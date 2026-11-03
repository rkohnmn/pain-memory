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
    page.add_init_script("""(() => {
      const request = window.requestAnimationFrame.bind(window);
      const cancel = window.cancelAnimationFrame.bind(window);
      window.__frameCount = 0;
      window.__pendingFrames = new Set();
      window.requestAnimationFrame = callback => {
        const id = request(time => { window.__pendingFrames.delete(id); window.__frameCount++; callback(time); });
        window.__pendingFrames.add(id); return id;
      };
      window.cancelAnimationFrame = id => { window.__pendingFrames.delete(id); cancel(id); };
      window.__setHiddenForTest = value => {
        Object.defineProperty(document, 'hidden', {configurable:true, get:() => value});
        document.dispatchEvent(new Event('visibilitychange'));
      };
    })()""")
    page.emulate_media(reduced_motion='reduce')
    page.goto(base)
    page.wait_for_timeout(150)
    assert page.evaluate('window.__pendingFrames.size') == 0
    assert page.evaluate('window.__frameCount') == 0
    expect(page.locator('.enter-btn')).to_be_visible()
    page.mouse.move(20, 20)
    assert page.locator('.parallax-layer').evaluate_all("els => els.every(el => el.style.transform === 'none')")
    page.emulate_media(reduced_motion='no-preference')
    page.wait_for_function('window.__frameCount > 3')
    page.evaluate('window.__setHiddenForTest(true)')
    assert page.evaluate('window.__pendingFrames.size') == 0
    count = page.evaluate('window.__frameCount')
    page.wait_for_timeout(300)
    assert page.evaluate('window.__frameCount') == count
    page.evaluate('window.__setHiddenForTest(false)')
    page.wait_for_function('(count) => window.__frameCount > count', arg=count)
    page.emulate_media(reduced_motion='reduce')
    page.wait_for_function('window.__pendingFrames.size === 0')
    count = page.evaluate('window.__frameCount')
    page.wait_for_timeout(300)
    assert page.evaluate('window.__frameCount') == count
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
