import allure
from selenium.webdriver.common.by import By
from final_work.pages.base_page import BasePage

class BonusPage(BasePage):
    """Страница бонусной программы"""

    url = "https://pizzeria.skillbox.cc/bonus/"

    @allure.step("Открыть страницу бонусной программы")
    def open_bonus_page(self, driver):
        driver.get(self.url)

    @allure.step("Ввести имя: {name}")
    def enter_name(self, driver, name):
        driver.find_element(By.ID, "bonus_username").send_keys(name)

    @allure.step("Ввести телефон: {phone}")
    def enter_phone(self, driver, phone):
        driver.find_element(By.ID, "bonus_phone").send_keys(phone)

    @allure.step("Нажать кнопку 'Оформить карту'")
    def click_activate(self, driver):
        driver.find_element(By.CSS_SELECTOR, "button[name='bonus']").click()

    @allure.step("Проверить, что активация прошла успешно")
    def is_activation_successful(self, driver):
        """Проверка сообщения об успешной активации"""
        try:
            success = driver.find_element(By.CSS_SELECTOR, "#bonus_main h3")
            return "оформлена" in success.text.lower()
        except:
            return False