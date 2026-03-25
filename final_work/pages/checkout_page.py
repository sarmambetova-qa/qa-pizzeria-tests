import allure
import time
from selenium.webdriver.common.by import By
from final_work.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    url = "https://pizzeria.skillbox.cc/checkout/"

    @allure.step("Открыть страницу оформления заказа")
    def open_checkout_page(self, driver):
        driver.get(self.url)
        time.sleep(2)

    @allure.step("Заполнить данные для доставки")
    def fill_shipping_details(self, driver, first_name, last_name, address, city, state, postcode, phone):
        """Заполнение формы доставки"""
        driver.find_element(By.ID, "billing_first_name").send_keys(first_name)
        driver.find_element(By.ID, "billing_last_name").send_keys(last_name)
        driver.find_element(By.ID, "billing_address_1").send_keys(address)
        driver.find_element(By.ID, "billing_city").send_keys(city)
        driver.find_element(By.ID, "billing_state").send_keys(state)
        driver.find_element(By.ID, "billing_postcode").send_keys(postcode)
        driver.find_element(By.ID, "billing_phone").send_keys(phone)

    @allure.step("Выбрать дату доставки {date}")
    def select_delivery_date(self, driver, date):
        """Выбор даты доставки"""
        try:
            date_input = driver.find_element(By.ID, "order_date")
            date_input.clear()
            date_input.send_keys(date)
            time.sleep(1)
        except:
            pass

    @allure.step("Добавить комментарий к заказу: {comment}")
    def add_order_comment(self, driver, comment):
        """Добавить комментарий к заказу (необязательно)"""
        try:
            comment_field = driver.find_element(By.ID, "order_comments")
            comment_field.send_keys(comment)
        except:
            pass

    @allure.step("Выбрать способ оплаты 'Оплата при доставке'")
    def select_cash_on_delivery(self, driver):
        """Выбор оплаты при доставке"""
        driver.find_element(By.ID, "payment_method_cod").click()

    @allure.step("Принять условия доставки")
    def accept_terms(self, driver):
        """Принять условия доставки (чекбокс)"""
        try:
            terms_checkbox = driver.find_element(By.ID, "terms")
            if not terms_checkbox.is_selected():
                terms_checkbox.click()
                time.sleep(1)
        except:
            pass

    @allure.step("Подтвердить заказ")
    def place_order(self, driver):
        """Нажать кнопку 'Оформить заказ'"""
        driver.find_element(By.ID, "place_order").click()
        time.sleep(3)

    @allure.step("Получить текст подтверждения заказа")
    def get_order_confirmation(self, driver):
        """Получить сообщение об успешном заказе"""
        try:
            # Ищем заголовок "ЗАКАЗ ПОЛУЧЕН"
            confirmation = driver.find_element(By.CSS_SELECTOR, "h2.post-title")
            return confirmation.text
        except:
            return ""

    @allure.step("Получить общую сумму заказа")
    def get_order_total(self, driver):
        """Получить итоговую сумму заказа"""
        try:
            total = driver.find_element(By.CSS_SELECTOR, ".order-total .amount, .woocommerce-order-overview .amount")
            total_text = total.text.replace('₽', '').replace(' ', '').strip()
            return float(total_text.replace(',', '.'))
        except:
            return 0
