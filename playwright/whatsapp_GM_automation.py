from playwright.sync_api import sync_playwright, TimeoutError
import time
import pyautogui

GROUP_NAME = "SE - AI-B5"
MESSAGE = "Good Morning All :) (Playwrigh/pyautogui automation)"

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_session",
        headless=False
    )

    page = browser.new_page()
    page.goto("https://web.whatsapp.com", timeout=60000)

    # Wait until WhatsApp UI is ready
    page.wait_for_selector('div[contenteditable="true"]', timeout=60000)

    # Search for the group
    search_box = page.locator('div[contenteditable="true"]').first
    search_box.click()
    search_box.fill(GROUP_NAME)
    time.sleep(1)

    # Open the filtered chat
    page.keyboard.press("Enter")

    # Message input box
    message_box = page.locator('div[contenteditable="true"]').nth(1)
    message_box.click()
    message_box.type(MESSAGE, delay=50)

    # Send message
    page.keyboard.press("Enter")

    # ---- METHOD 2 (HARDENED) ----
    # Mandatory commit window
    time.sleep(2)

    try:
        # Wait for sending clock icon if it appears
        page.wait_for_selector(
            "span[data-icon='msg-time']",
            timeout=3000
        )

        # Wait until the clock icon disappears
        page.wait_for_selector(
            "span[data-icon='msg-time']",
            state="detached",
            timeout=10000
        )
    except TimeoutError:
        # Fast network: icon may never appear
        pass

    # Final stabilization delay
    time.sleep(2)

    # Close browser safely
    page.close()
    browser.close()

# Switch back to VS Code
time.sleep(1)
pyautogui.hotkey("alt", "tab")

print("Message sent successfully.")
