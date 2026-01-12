import asyncio
import time
from pathlib import Path
from typing import Tuple

from app.models.capture import ArchiveResult


async def archive_page(url: str, capture_id: str, timeout_ms: int = 30000) -> ArchiveResult:
    start_time = time.time()

    try:
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1280, "height": 800},
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            )

            page = await context.new_page()
            page.set_default_timeout(timeout_ms)

            await page.goto(url, wait_until="networkidle")

            title = await page.title()

            screenshot_bytes = await page.screenshot(full_page=True, type="png")

            html_content = await page.content()

            await browser.close()

            elapsed_ms = int((time.time() - start_time) * 1000)

            return ArchiveResult(
                success=True,
                html_path=f"captures/{capture_id}/page.html",
                screenshot_path=f"captures/{capture_id}/screenshot.png",
                elapsed_ms=elapsed_ms,
            )

    except Exception as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return ArchiveResult(
            success=False,
            error=str(e),
            elapsed_ms=elapsed_ms,
        )


async def capture_screenshot(url: str, timeout_ms: int = 10000) -> Tuple[bytes | None, str | None]:
    try:
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            page.set_default_timeout(timeout_ms)

            await page.goto(url, wait_until="domcontentloaded")
            screenshot = await page.screenshot(type="png")

            await browser.close()
            return screenshot, None

    except Exception as e:
        return None, str(e)


async def extract_metadata(url: str, timeout_ms: int = 5000) -> dict:
    try:
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            page.set_default_timeout(timeout_ms)

            await page.goto(url, wait_until="domcontentloaded")

            metadata = await page.evaluate("""() => {
                const getMeta = (name) => {
                    const el = document.querySelector(`meta[name="${name}"], meta[property="${name}"]`);
                    return el ? el.content : null;
                };
                
                return {
                    title: document.title,
                    description: getMeta('description') || getMeta('og:description'),
                    image: getMeta('og:image'),
                    author: getMeta('author'),
                    published: getMeta('article:published_time'),
                    siteName: getMeta('og:site_name'),
                };
            }""")

            await browser.close()
            return metadata

    except Exception as e:
        return {"error": str(e)}
