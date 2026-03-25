import allure
import time
from selenium.webdriver.common.by import By
from final_work.pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины"""
    url = "https://pizzeria.skillbox.cc/cart/"

    @allure.step("Открыть страницу корзины")
    def open_cart_page(self, driver):
        driver.get(self.url)
        time.sleep(2)

    @allure.step("Получить все товары в корзине")
    def get_all_cart_items(self, driver):
        return driver.find_elements(By.CSS_SELECTOR, ".cart_item")

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self, driver):
        return len(self.get_all_cart_items(driver))

    @allure.step("Изменить количество товара {index} на {quantity}")
    def change_quantity(self, driver, index=0, quantity=1):
        items = self.get_all_cart_items(driver)
        if len(items) > index:
            qty_input = items[index].find_element(By.CSS_SELECTOR, ".qty")
            qty_input.clear()
            qty_input.send_keys(str(quantity))

    @allure.step("Обновить корзину")
    def update_cart(self, driver):
        driver.find_element(By.CSS_SELECTOR, "input[name='update_cart']").click()

    @allure.step("Удалить товар {index} из корзины")
    def remove_item(self, driver, index=0):
        items = self.get_all_cart_items(driver)
        if len(items) > index:
            remove_btn = items[index].find_element(By.CSS_SELECTOR, ".remove")
            remove_btn.click()

    @allure.step("Перейти к оформлению заказа")
    def go_to_checkout(self, driver):
        driver.find_element(By.CSS_SELECTOR, ".checkout-button").click()

    @allure.step("Получить общую сумму корзины")
    def get_total(self, driver):
        """Получить итоговую сумму корзины"""
        try:
            # Ищем элемент с суммой
            total_element = driver.find_element(By.CSS_SELECTOR, ".order-total .amount")
            total_text = total_element.text
            # Очищаем от лишнего (убираем "СУММА" если есть)
            total_text = total_text.replace('СУММА', '').replace('₽', '').replace(' ', '').strip()
            return float(total_text.replace(',', '.'))
        except:
            # Если не нашли .order-total, ищем .cart-total
            try:
                total_element = driver.find_element(By.CSS_SELECTOR, ".cart-total .amount")
                total_text = total_element.text
                total_text = total_text.replace('₽', '').replace(' ', '').strip()
                return float(total_text.replace(',', '.'))
            except:
                return 0

    @allure.step("Применить промокод {coupon}")
    def apply_coupon(self, driver, coupon):
        driver.find_element(By.ID, "coupon_code").send_keys(coupon)
        driver.find_element(By.CSS_SELECTOR, "button[name='apply_coupon']").click()
        time.sleep(2)

    @allure.step("Получить сообщение о промокоде")
    def get_coupon_message(self, driver):
        try:
            message = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message, .woocommerce-error")
            return message.text
        except:
            return ""

    @allure.step("Проверить, что корзина пуста")
    def is_cart_empty(self, driver):
        try:
            empty = driver.find_element(By.CSS_SELECTOR, ".cart-empty")
            return empty.is_displayed()
        except:
            return False