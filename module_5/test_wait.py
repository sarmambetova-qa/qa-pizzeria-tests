import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def test_wait_page_load(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        pass

    def test_wait_types(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com')
        WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        )

    def test_wait_dialog(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://m1vcki.csb.app/')
        WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.ID, 'name'))
        driver.find_element(By.ID, 'name').send_keys('skillbox')
        driver.find_element(By.ID, 'email').send_keys('skillbox@mail.ru')
        driver.find_element(By.NAME, 'password').send_keys('skillbox')
        driver.execute_script('document.activeElement.blur()')
        driver.find_element(By.CSS_SELECTOR, '[role="checkbox"]').click()
        driver.find_element(By.XPATH, '//button/span[contains(text(), "Submit")]').click()
        WebDriverWait(driver, timeout=5).until(
            lambda d: d.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]')
        )
        driver.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]').click()
        pass
