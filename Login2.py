import re
from playwright.sync_api import Page, expect


def test_comet(page: Page): page.goto("https://www.comet.com/site/")

# Expect a title "to contain" a substring.
expect(page).to_have_title(re.compile("Comet"))

page.get_by_role("navigation", name="Main menu").get_by_role("link", name="Login").click()
page.wait_for_url("https://www.comet.com/login")
page.get_by_placeholder("user@example.com").click()
page.get_by_placeholder("user@example.com").fill("mikam@comet.com")
page.get_by_placeholder("******").click()
page.get_by_placeholder("******").fill("Yomo111!!!")
page.get_by_role("button", name="Login").click()
page.wait_for_url("https://www.comet.com/mikam#projects")
# ---------------------
#browser.close()