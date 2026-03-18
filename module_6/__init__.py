import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from module_6.src.actions.components.forms import fill_forms
from module_6.src.helpers.accounts_base import AccountsBase


class TestWait(AccountsBase):
    def test_wait_page_load(self, selenium, go_to_github): # явное ожидание
        selenium.get('https://github.com')
        selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        pass

    def test_wait_types(self, selenium, go_to_github): # неявное ожидание
        selenium.get('https://github.com')
        # selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        WebDriverWait(selenium, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        )
        pass

    def test_wait_dialog(self, selenium):
        selenium.get('https://m1vcki.csb.app/')
        time.sleep(10)
        WebDriverWait(selenium, timeout=30).until(lambda d: d.find_element(By.ID, "name"))
        fill_forms(selenium, name="awesome_skillbox")

        # selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        WebDriverWait(selenium, timeout=5).until(
            lambda d: d.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]')
        )
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]').click()

        pass
