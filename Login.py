from playwright.sync_api import Playwright, sync_playwright, expect
from idlelib import browser

import unittest

def run(playwright: Playwright) -> None: browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto("https://demo.playwright.dev/todomvc/")
page.goto("https://demo.playwright.dev/todomvc/#/")
page.goto("https://www.comet.com/site/")
page.get_by_role("navigation", name="Main menu").get_by_role("link", name="Login").click()
page.wait_for_url("https://www.comet.com/login")
page.get_by_placeholder("user@example.com").click()
page.get_by_placeholder("user@example.com").fill("mikam@comet.com")
page.get_by_placeholder("******").click()
page.get_by_placeholder("******").fill("Yomo111!!!")
page.get_by_role("button", name="Login").click()
page.wait_for_url("https://www.comet.com/mikam#projects")
# ---------------------
context.close()
browser.close()

with sync_playwright() as playwright: run(playwright)