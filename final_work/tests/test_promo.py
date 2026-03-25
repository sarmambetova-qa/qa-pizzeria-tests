import time
import allure
import random
from selenium.webdriver.common.by import By
from final_work.pages.main_page import MainPage
from final_work.pages.cart_page import CartPage
from final_work.pages.auth_page import AuthPage
from final_work.pages.checkout_page import CheckoutPage


@allure.epic("Пиццерия")
@allure.feature("Промокоды")
class TestPromo:

    @allure.story("Проверка валидного промокода")
    @allure.title("Тест промокода GIVEMEHALYAVA: скидка 10%")
    def test_valid_promo(self, driver):
        """Сценарий №1: Применить промокод GIVEMEHALYAVA"""
        main_page = MainPage()
        cart_page = CartPage()
        auth_page = AuthPage()
        checkout_page = CheckoutPage()

        # Данные для регистрации
        random_num = random.randint(1000, 9999)
        username = f"user{random_num}"
        email = f"user{random_num}@mail.ru"
        password = "Test123456"

        # 1. Открыть главную страницу и добавить пиццу в корзину
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page(driver)
            time.sleep(2)

        with allure.step("Добавить пиццу в корзину"):
            main_page.add_pizza_to_cart(driver, index=0)
            time.sleep(2)

        # 2. Перейти в корзину
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        # 3. Запомнить сумму до применения промокода
        with allure.step("Запомнить сумму до промокода"):
            original_total = cart_page.get_total(driver)
            print(f"Сумма до промокода: {original_total}")

        # 4. Применить промокод GIVEMEHALYAVA
        with allure.step("Применить промокод GIVEMEHALYAVA"):
            cart_page.apply_coupon(driver, "GIVEMEHALYAVA")
            time.sleep(2)

        # 5. Проверить, что сумма уменьшилась на 10%
        with allure.step("Проверить, что сумма уменьшилась на 10%"):
            new_total = cart_page.get_total(driver)
            print(f"Сумма после промокода: {new_total}")
            expected_total = original_total * 0.9
            assert abs(new_total - expected_total) < 0.01, \
                f"Ожидалось {expected_total}, получено {new_total}"
            print("Промокод применился успешно!")

        print("Тест пройден!")


    @allure.story("Проверка неверного промокода")
    @allure.title("Тест промокода DC120: скидка не применяется")
    def test_invalid_promo(self, driver):
        """Сценарий №2: Применить неверный промокод"""
        main_page = MainPage()
        cart_page = CartPage()

        # 1. Открыть главную страницу и добавить пиццу
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page(driver)
            time.sleep(2)

        with allure.step("Добавить пиццу в корзину"):
            main_page.add_pizza_to_cart(driver, index=0)
            time.sleep(2)

        # 2. Перейти в корзину
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        # 3. Запомнить сумму
        with allure.step("Запомнить сумму"):
            original_total = cart_page.get_total(driver)
            print(f"Сумма: {original_total}")

        # 4. Применить неверный промокод
        with allure.step("Применить промокод DC120"):
            cart_page.apply_coupon(driver, "DC120")
            time.sleep(2)

        # 5. Проверить, что сумма не изменилась
        with allure.step("Проверить, что сумма не изменилась"):
            new_total = cart_page.get_total(driver)
            assert abs(new_total - original_total) < 0.01, "Сумма изменилась, хотя промокод неверный"
            print("Сумма не изменилась, промокод не применился")

        # 6. Проверить сообщение об ошибке
        with allure.step("Проверить сообщение об ошибке"):
            message = cart_page.get_coupon_message(driver)
            assert "неверный" in message.lower(), \
                f"Нет сообщения об ошибке: {message}"
            print(f"Сообщение об ошибке: {message}")

        print("Тест пройден!")

    @allure.story("Проверка однократного применения промокода")
    @allure.title("Тест: промокод GIVEMEHALYAVA работает только один раз")
    def test_promo_one_time(self, driver):
        """Сценарий №4: Промокод должен сработать только один раз для пользователя"""
        main_page = MainPage()
        cart_page = CartPage()
        auth_page = AuthPage()
        checkout_page = CheckoutPage()

        # Уникальные данные для регистрации
        random_num = random.randint(1000, 9999)
        username = f"user{random_num}"
        email = f"user{random_num}@mail.ru"
        password = "Test123456"

        first_name = "Иван"
        last_name = "Петров"
        address = "ул. Петрова, д.6"
        city = "Москва"
        state = "Москва"
        postcode = "123456"
        phone = "89151234567"

        # 1. Открыть главную страницу и добавить пиццу
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page(driver)
            time.sleep(2)

        with allure.step("Добавить пиццу в корзину"):
            main_page.add_pizza_to_cart(driver, index=0)
            time.sleep(2)

        # 2. Перейти в корзину и применить промокод
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        with allure.step("Применить промокод GIVEMEHALYAVA"):
            cart_page.apply_coupon(driver, "GIVEMEHALYAVA")
            time.sleep(2)

        # 3. Запомнить сумму после промокода
        with allure.step("Запомнить сумму"):
            total_with_promo = cart_page.get_total(driver)
            print(f"Сумма с промокодом: {total_with_promo}")

        # 4. Зарегистрироваться и оформить заказ
        with allure.step("Перейти к оформлению заказа"):
            cart_page.go_to_checkout(driver)
            time.sleep(2)

        with allure.step("Перейти в Мой аккаунт"):
            driver.find_element(By.CSS_SELECTOR, "a[href*='/my-account/']").click()
            time.sleep(2)

        with allure.step("Нажать кнопку 'Зарегистрироваться'"):
            auth_page.go_to_register_page(driver)

        with allure.step("Зарегистрировать нового пользователя"):
            auth_page.register(driver, username, email, password)
            time.sleep(3)

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart(driver)
            time.sleep(2)

        with allure.step("Перейти к оформлению заказа"):
            cart_page.go_to_checkout(driver)
            time.sleep(2)

        with allure.step("Заполнить данные для доставки"):
            checkout_page.fill_shipping_details(
                driver, first_name, last_name, address, city, state, postcode, phone
            )
            time.sleep(1)

        with allure.step("Выбрать оплату при доставке"):
            checkout_page.select_cash_on_delivery(driver)

        with allure.step("Принять условия доставки"):
            checkout_page.accept_terms(driver)

        with allure.step("Подтвердить заказ"):
            checkout_page.place_order(driver)
            time.sleep(3)

        # 5. Проверить, что заказ оформлен
        with allure.step("Проверить, что заказ оформлен успешно"):
            confirmation = checkout_page.get_order_confirmation(driver)
            assert "получен" in confirmation.lower(), f"Заказ не оформлен: {confirmation}"
            print("Первый заказ оформлен")

        # 6. Сделать второй заказ с тем же промокодом
        with allure.step("Добавить пиццу в корзину для второго заказа"):
            main_page.open_main_page(driver)
            time.sleep(2)
            main_page.add_pizza_to_cart(driver, index=0)
            time.sleep(2)
            main_page.go_to_cart(driver)
            time.sleep(2)

        # Запоминаем исходную сумму второго заказа (без промокода)
        original_total_second = cart_page.get_total(driver)
        print(f"Исходная сумма второго заказа: {original_total_second}")

        with allure.step("Повторно применить промокод GIVEMEHALYAVA"):
            cart_page.apply_coupon(driver, "GIVEMEHALYAVA")
            time.sleep(2)

        # 7. Проверить, что промокод не сработал (сумма не изменилась)
        with allure.step("Проверить, что промокод не применился"):
            total_second = cart_page.get_total(driver)
            print(f"Сумма второго заказа после промокода: {total_second}")
            assert abs(total_second - original_total_second) < 0.01, \
                f"Промокод сработал! Сумма изменилась: {original_total_second} -> {total_second}"
            print("Промокод не применился второй раз — всё верно")

        print("Тест пройден!")
