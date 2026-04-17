#!/usr/bin/env python3
"""
Screenshot logo showcase HTML using Playwright
Usage: python screenshot_showcase.py <html_path> <output_png_path> [--viewport-width=1400] [--viewport-height=2000]
"""

import argparse
import subprocess
import sys
import time
import os

def main():
    parser = argparse.ArgumentParser(description='Screenshot logo showcase HTML')
    parser.add_argument('html_path', help='Path to HTML file')
    parser.add_argument('output_path', help='Output PNG path')
    parser.add_argument('--viewport-width', type=int, default=1400, help='Viewport width')
    parser.add_argument('--viewport-height', type=int, default=2000, help='Viewport height')
    parser.add_argument('--port', type=int, default=8765, help='HTTP server port')
    args = parser.parse_args()

    html_path = os.path.abspath(args.html_path)
    output_path = os.path.abspath(args.output_path)
    workdir = os.path.dirname(html_path)
    filename = os.path.basename(html_path)

    # Start HTTP server in background
    server_cmd = f"cd {workdir} && python3 -m http.server {args.port}"
    server_proc = subprocess.Popen(
        server_cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Wait for server to start
    time.sleep(2)

    try:
        # Use playwright to screenshot
        screenshot_cmd = [
            "npx", "playwright", "screenshot",
            "--browser=chromium",
            f"--viewport-size={args.viewport_width},{args.viewport_height}",
            f"http://localhost:{args.port}/{filename}",
            output_path
        ]

        result = subprocess.run(screenshot_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        print(f"Screenshot saved to: {output_path}")

    finally:
        # Cleanup server
        server_proc.terminate()
        server_proc.wait()

if __name__ == "__main__":
    main()
