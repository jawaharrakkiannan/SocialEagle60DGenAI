from playwright.async_api import async_playwright
import asyncio
from datetime import datetime

async def google_search_screenshot(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.google.com")

        # Type search query and submit
        await page.fill("textarea[name='q']", query)
        await page.keyboard.press("Enter")

        # Wait for results
        await page.wait_for_load_state("networkidle")

        # Screenshot with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"google_search_{timestamp}.png"

        await page.screenshot(path=filename, full_page=True)
        print(f"Screenshot saved as {filename}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(google_search_screenshot("Playwright Python automation"))
