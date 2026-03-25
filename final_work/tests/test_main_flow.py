import time
import allure
import random
from selenium.webdriver.common.by import By
from final_work.pages.main_page import MainPage
from final_work.pages.cart_page import CartPage
from final_work.pages.auth_page import AuthPage
from final_work.pages.checkout_page import CheckoutPage


@allure.epic("Пиццерия")
@allure.feature("Основной флоу клиента")
class TestMainFlow:

    @allure.story("Полный цикл заказа")
    @allure.title("Тест основного флоу: выбор пиццы, корзина, регистрация, оформление")
    def test_main_flow(self, driver):
        main_page = MainPage()
        cart_page = CartPage()
        auth_page = AuthPage()
        checkout_page = CheckoutPage()

        random_num = random.randint(1000, 9999)
        username = f"user{random_num}"
        email = f"user{random_num}@mail.ru"
        password = "Test123456"

        print(f"Регистрируем пользователя: {username}")

        first_name = "Иван"
        last_name = "Петров"
        address = "ул. Петрова, д.6"
        city = "Москва"
        state = "Москва"
        postcode = "123456"
        phone = "89151234567"

        # 1. Открыть главную страницу
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page(driver)
            time.sleep(2)

        # 2. Добавить пиццу в корзину
        with allure.step("Добавить первую пиццу в корзину"):
            main_page.add_pizza_to_cart(driver, index=0)
            time.sleep(2)

        # 3. Перейти в корзину
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        # 4. Проверить, что товар добавился
        with allure.step("Проверить, что товар в корзине"):
            items_count = cart_page.get_cart_items_count(driver)
            assert items_count > 0, "Корзина пуста"
            print(f"Товаров в корзине: {items_count}")

        # 5. Перейти к оформлению заказа (нажать "Перейти к оплате")
        with allure.step("Перейти к оформлению заказа"):
            cart_page.go_to_checkout(driver)
            time.sleep(2)

        # 6. Перейти в "Мой аккаунт" через меню
        with allure.step("Перейти в Мой аккаунт"):
            driver.find_element(By.CSS_SELECTOR, "a[href*='/my-account/']").click()
            time.sleep(2)

        # 7. Нажать кнопку "Зарегистрироваться"
        with allure.step("Нажать кнопку 'Зарегистрироваться'"):
            auth_page.go_to_register_page(driver)

        # 8. Зарегистрировать пользователя
        with allure.step("Зарегистрировать нового пользователя"):
            auth_page.register(driver, username, email, password)
            time.sleep(3)
            print(f"Текущий URL после регистрации: {driver.current_url}")
            print(f"Заголовок страницы: {driver.title}")

            # Проверяем, есть ли сообщение об ошибке
            try:
                error_msg = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error").text
                print(f"Ошибка регистрации: {error_msg}")
            except:
                print("Сообщений об ошибке не найдено")

        # 9. Перейти в "Мой аккаунт"
        with allure.step("Перейти в Мой аккаунт"):
            driver.get("https://pizzeria.skillbox.cc/my-account/")
            time.sleep(3)

        # 10. Проверить, что пользователь залогинен (по тексту "Привет")
        with allure.step("Проверить, что пользователь залогинен"):
            page_text = driver.page_source
            assert "Привет" in page_text or "Выйти" in page_text, "Пользователь не залогинен"
            print("Пользователь залогинен")

        # 11. Перейти в корзину
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        # 12. Перейти к оформлению заказа
        with allure.step("Перейти к оформлению заказа"):
            cart_page.go_to_checkout(driver)
            time.sleep(2)

        # 13. Заполнить данные для доставки
        with allure.step("Заполнить данные для доставки"):
            checkout_page.fill_shipping_details(
                driver, first_name, last_name, address, city, state, postcode, phone
            )
            time.sleep(1)

        # 14. Выбрать оплату при доставке
        with allure.step("Выбрать оплату при доставке"):
            checkout_page.select_cash_on_delivery(driver)

        # 15. Принять условия
        with allure.step("Принять условия доставки"):
            checkout_page.accept_terms(driver)

        # 16. Подтвердить заказ
        with allure.step("Подтвердить заказ"):
            checkout_page.place_order(driver)
            time.sleep(3)

        # 17. Проверить, что заказ оформлен
        with allure.step("Проверить, что заказ оформлен успешно"):
            confirmation = checkout_page.get_order_confirmation(driver)
            assert "получен" in confirmation.lower() or "заказ" in confirmation.lower(), \
                f"Сообщение о подтверждении не найдено: {confirmation}"
            print(f"Заказ оформлен: {confirmation}")

        print("Тест основного флоу успешно пройден!")
