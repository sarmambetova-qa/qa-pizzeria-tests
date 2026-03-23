import logging.config
from os import path
import pytest
from playwright.sync_api import sync_playwright

# lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
# logging.config.fileConfig(lof_file_path)

pytest_plugins = [
    "module_7.src.actions.base",
    "module_7.src.actions.wait"
]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub url")
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("browser_version", "Browser version for tests")
    parser.addini("headless", "Run browser in headless node")


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        yield browser
        browser.close()


@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
