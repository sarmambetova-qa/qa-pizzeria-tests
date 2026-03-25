import logging.config
from os import path
import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(lof_file_path)


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub url")
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("browser_version", "Browser version for tests")
    parser.addini("headless", "Run browser in headless mode")


def pytest_configure(config):
    """Настройка логирования"""
    pass


@pytest.fixture(scope="function")
def driver(pytestconfig):
    options = Options()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f"Prepare {browser_name} browser...")

    if pytestconfig.getini("headless") == 'True' and browser_name == "chrome":
        options.add_argument("--headless")

    options.add_argument("--start-maximized")

    options.set_capability("browserName", pytestconfig.getini("browser_name"))
    options.set_capability("browserVersion", pytestconfig.getini("browser_version"))
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver = Remote(
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    logging.info(f"Browser {browser_name} has been started.")

    yield driver
    driver.quit()