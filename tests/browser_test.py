"""Headless Chromium regression checks. See BROWSER_TESTS.md."""
import csv
import io
import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[1]

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def translate_path(self, path):
        return super().translate_path(path.removeprefix("/preview"))


def check(page, context, base):
    page.goto(base)
    page.evaluate('window.open = () => null')
    page.locator('.enter-btn').click()
    page.wait_for_url('**/portal.html')
    expect(page).to_have_title('Portal – Pain and Memory')


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as pw:
            executable = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE")
            browser = pw.chromium.launch(headless=True, **({"executable_path": executable} if executable else {}))
            context = browser.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            try:
                check(page, context, f"http://127.0.0.1:{server.server_port}/preview/")
                assert not errors, errors
                print("Browser regressions passed")
            except Exception:
                artifacts = ROOT / "test-results"
                artifacts.mkdir(exist_ok=True)
                page.screenshot(path=str(artifacts / "failure.png"), full_page=True)
                context.tracing.stop(path=str(artifacts / "trace.zip"))
                raise
            finally:
                context.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


if __name__ == "__main__":
    main()
