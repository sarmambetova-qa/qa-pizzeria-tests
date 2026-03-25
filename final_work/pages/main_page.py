import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from final_work.pages.base_page import BasePage


class MainPage(BasePage):
    url = "https://pizzeria.skillbox.cc/"

    @allure.step("Открыть главную страницу")
    def open_main_page(self, driver):
        driver.get(self.url)
        time.sleep(3)

    @allure.step("Добавить пиццу в корзину {index}")
    def add_pizza_to_cart(self, driver, index=0):
        # Находим все пиццы
        pizzas = driver.find_elements(By.CSS_SELECTOR, ".item-img")
        if len(pizzas) > index:
            # Прокручиваем к пицце
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pizzas[index])
            time.sleep(1)

            # Находим кнопку "В корзину" внутри этой пиццы
            cart_button = pizzas[index].find_element(By.CSS_SELECTOR, ".ajax_add_to_cart")

            # Кликаем через JavaScript
            driver.execute_script("arguments[0].click();", cart_button)
            time.sleep(1)

    @allure.step("Перейти в корзину")
    def go_to_cart(self, driver):
        driver.find_element(By.CSS_SELECTOR, "div.right-header a[href*='/cart/']").click()
        time.sleep(2)
