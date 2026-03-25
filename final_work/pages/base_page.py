import allure
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для всех страниц"""

    @allure.step("Открыть страницу {url}")
    def open(self, driver, url):
        driver.get(url)

    @allure.step("Получить заголовок страницы")
    def get_title(self, driver):
        return driver.title

    def wait_for_element(self, driver, by, selector, timeout=10):
        """Ожидание появления элемента"""
        return WebDriverWait(driver, timeout).until(
            lambda d: d.find_element(by, selector)
        )