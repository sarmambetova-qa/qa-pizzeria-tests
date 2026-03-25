import time
import allure
from selenium.webdriver.common.by import By
from final_work.pages.bonus_page import BonusPage


@allure.epic("Пиццерия")
@allure.feature("Бонусная программа")
class TestBonus:

    @allure.story("Проверка бонусной программы")
    @allure.title("Тест: регистрация в бонусной программе")
    def test_bonus_registration(self, driver):
        """Тест бонусной программы: ввод данных и активация"""
        bonus_page = BonusPage()

        # Уникальные данные для теста
        import random
        name = f"Тест{random.randint(100, 999)}"
        phone = f"8915{random.randint(1000000, 9999999)}"

        # 1. Открыть страницу бонусной программы
        with allure.step("Открыть страницу бонусной программы"):
            bonus_page.open_bonus_page(driver)
            time.sleep(2)

        # 2. Ввести имя
        with allure.step(f"Ввести имя: {name}"):
            bonus_page.enter_name(driver, name)
            time.sleep(1)

        # 3. Ввести телефон
        with allure.step(f"Ввести телефон: {phone}"):
            bonus_page.enter_phone(driver, phone)
            time.sleep(1)

        # 4. Нажать кнопку "Оформить карту"
        with allure.step("Нажать кнопку 'Оформить карту'"):
            bonus_page.click_activate(driver)
            time.sleep(2)

            # Обработка всплывающего окна (alert)
            try:
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert текст: {alert_text}")
                alert.accept()  # нажимаем OK
                time.sleep(2)
            except:
                print("Alert не появился")

        # 5. Проверить, что активация прошла успешно
        with allure.step("Проверить, что активация прошла успешно"):
            # Ждём появления сообщения на странице
            time.sleep(2)
            page_text = driver.page_source
            assert "оформлена" in page_text.lower(), "Активация не прошла успешно"
            print("Бонусная карта успешно оформлена!")