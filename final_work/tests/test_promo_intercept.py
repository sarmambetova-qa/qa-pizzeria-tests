import time
import allure
from playwright.sync_api import sync_playwright


@allure.epic("Пиццерия")
@allure.feature("Промокоды")
class TestPromoIntercept:

    @allure.story("Ошибка сервера при валидации промокода")
    @allure.title("Тест: при ошибке сервера промокод не применяется (Playwright)")
    def test_promo_server_error(self):
        """Сценарий №3: Перехват запроса и блокировка"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, args=['--start-maximized'])
            page = browser.new_page()

            # 1. Добавить пиццу в корзину напрямую через URL
            page.goto("https://pizzeria.skillbox.cc/?add-to-cart=425")
            time.sleep(2)

            # 2. Перейти в корзину
            page.goto("https://pizzeria.skillbox.cc/cart/")
            time.sleep(2)

            # 3. Запомнить сумму
            total_before = page.inner_text(".order-total .amount")
            print(f"Сумма до промокода: {total_before}")

            # 4. Перехватываем POST запрос к /cart/ и блокируем
            def intercept_request(route):
                if route.request.method == "POST" and "/cart/" in route.request.url:
                    print("Запрос перехвачен и заблокирован")
                    route.abort()
                else:
                    route.continue_()

            page.route("**/cart/**", intercept_request)

            # 5. Применить промокод
            page.fill("#coupon_code", "GIVEMEHALYAVA")
            page.click("button[name='apply_coupon']")
            time.sleep(3)

            # 6. Проверить, что сумма не изменилась
            total_after = page.inner_text(".order-total .amount")
            print(f"Сумма после промокода: {total_after}")

            assert total_before == total_after, f"Сумма изменилась: {total_before} -> {total_after}"
            print("Промокод не применился — тест пройден")

            # 7. Проверить сообщение об ошибке
            try:
                error_msg = page.inner_text(".woocommerce-error")
                print(f"Сообщение об ошибке: {error_msg}")
                assert error_msg != "", "Нет сообщения об ошибке"
            except:
                print("Сообщение об ошибке не найдено")

            browser.close()
