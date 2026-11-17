#!/usr/bin/env python3
"""Render a deterministic HTML animation to a teaser clip.

usage: python3 render.py <dir-with-index.html> <out-basename> [--still T ...]

The page must be 640x448 and define:
  window.DURATION            seconds (7 to 10)
  window.renderAt(t)         draw the frame for time t (seconds), synchronously, no wall-clock state
Needs Python playwright and ffmpeg with libx264 (on PATH, or its path in $FFMPEG).
Writes <out-basename>.mp4 (H.264, 30fps, 640x448, muted) and <out-basename>.jpg (first frame).
With --still T1 T2 ..., writes only PNG stills <dir>/still_<T>.png (for checking frames) and no video.
"""
import os, shutil, subprocess, sys, pathlib
from playwright.sync_api import sync_playwright

FFMPEG = os.environ.get("FFMPEG") or shutil.which("ffmpeg") or sys.exit("set FFMPEG to an ffmpeg binary with libx264")
W, H, FPS = 640, 448, 30

def main():
    src = pathlib.Path(sys.argv[1]).resolve()
    out = pathlib.Path(sys.argv[2]).resolve()
    stills = [float(x) for x in sys.argv[4:]] if len(sys.argv) > 3 and sys.argv[3] == "--still" else None
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((src / "index.html").as_uri())
        pg.evaluate("document.fonts.ready.then(() => true)")
        pg.wait_for_function("typeof window.renderAt === 'function' && window.DURATION > 0")
        dur = float(pg.evaluate("window.DURATION"))
        if stills is not None:
            for t in stills:
                pg.evaluate("t => window.renderAt(t)", min(t, dur))
                pg.screenshot(path=str(src / f"still_{t:g}.png"))
            print("stills written; duration", dur, "errors:", errs)
            b.close(); return
        n = round(dur * FPS) + 1
        ff = subprocess.Popen([FFMPEG, "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
            "-c:v", "png", "-i", "-", "-vf", f"scale={W}:{H}:flags=lanczos,format=yuv420p", "-an",
            "-c:v", "libx264", "-crf", "24", "-preset", "veryslow", "-tune", "animation",
            "-movflags", "+faststart", str(out) + ".mp4"], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate("t => window.renderAt(t)", min(i / FPS, dur))
            png = pg.screenshot()
            if i == 0:
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "image2pipe", "-c:v", "png", "-i", "-",
                    "-vf", f"scale={W}:{H}:flags=lanczos", "-q:v", "3", str(out) + ".jpg"], input=png, check=True)
            ff.stdin.write(png)
        ff.stdin.close(); ff.wait()
        b.close()
    mp4 = pathlib.Path(str(out) + ".mp4")
    print(f"{mp4} {mp4.stat().st_size/1024:.0f} KB, {dur:.1f}s, {n} frames; page errors: {errs}")

main()
