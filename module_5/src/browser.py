import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up_browser():
    options = Options()
    options.page_load_strategy = 'normal'

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # driver.maximize_window()

    yield driver
    time.sleep(3)
    driver.quit()
    print("Браузер закрыт")