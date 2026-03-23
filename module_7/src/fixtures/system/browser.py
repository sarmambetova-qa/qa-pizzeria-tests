import logging
from selenium.webdriver import Remote
import pytest
from selenium.webdriver.chrome.options import Options
import allure

@pytest.fixture(scope='class')
def selenium(pytestconfig):

    options = Options()
    options.page_load_strategy = 'normal'
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f"Prepare {browser_name} browser...")

    if pytestconfig.getini("headless") == 'True' and browser_name == "chrome":
        options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")

    with allure.step('Запуск браузера'):
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
    logging.info(f"Close {browser_name} browser...")
    driver.quit()
