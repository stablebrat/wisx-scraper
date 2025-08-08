from playwright.sync_api import sync_playwright
import time
import os

def get_dispatch_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(accept_downloads=True)  # Enable download handling
        page = context.new_page()

        print("🔐 Navigating to login page...")
        page.goto("https://wisx.aaveg.co.in/", timeout=60000)
        page.wait_for_selector("#Email")

        print("🧠 Typing in username...")
        page.fill("#Email", "WISX_USERNAME")
        page.keyboard.press("Tab")
        time.sleep(1)

        print("🔐 Typing in password...")
        page.fill("#Password", "WISX_PASSWORD")

        print("✅ Checking Remember Me...")
        page.check("#RememberMe")
        time.sleep(1)

        print("🚀 Submitting login...")
        page.click('input[type="submit"][value="Log in"]')

        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except:
            print("⚠️ Timeout waiting for page load.")

        if page.url == "https://wisx.aaveg.co.in/":
            print("❌ Login failed — still on login page.")
            browser.close()
            return []

        print("✅ Login successful. Going to report...")

        page.goto("https://wisx.aaveg.co.in/Report/DIS_406_DispatchDetails?rptid_c=51", timeout=60000)
        page.wait_for_selector("text=Export", timeout=15000)
        print("karthik")
        # Optionally wait a moment for the data to populate
        time.sleep(2)
        print("karthik")
        print("📤 Clicking Export to download file...")

        with page.expect_download() as download_info:
            page.click("text=Export")  # Or you can use a better selector if needed

        download = download_info.value
        download_path = os.path.join(os.getcwd(), "dispatch_report.xlsx")
        download.save_as(download_path)

        print(f"✅ File downloaded and saved to: {download_path}")

        browser.close()
        return download_path  # Return path to use elsewhere
