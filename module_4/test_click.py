from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClick:
    def test_click(self, set_up_browser):  # клик кнопки
        driver = set_up_browser
        driver.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')  # отображаются кнопки
        driver.find_element(By.XPATH, '//button/span[contains(text(), "Primary")]').click() # находим соответствующий элемент

    def test_click(self, set_up_browser):  #(клик с ошибкой)не может произойти, так как его перекрывает другой элемент (плашка)
        driver = set_up_browser
        driver.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')  # отображаются кнопки
        driver.find_element(By.XPATH, '//button').click() # находим соответствующий элемент


    def test_double_click(self, set_up_browser):  # двойной клик (двойное нажатие на кнопку)
        driver = set_up_browser
        driver.get('https://l8c7w2.csb.app/demo/ButtonDemo.html')  # отображаются кнопки
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(driver.find_element(By.XPATH, '//button/span[contains(text(), "Multiple")]')).perform()

    def test_checkbox(self, set_up_browser):  # клик в чекбокс
        driver = set_up_browser
        driver.get('https://bn6oef.csb.app/demo/CheckboxDemo.html')
        driver.find_element(By.CSS_SELECTOR, '[for="city1"]').click()
        driver.find_element(By.CSS_SELECTOR, '[for="city2"]').click()
        pass

    def test_radio(self, set_up_browser):  # клик радио-батон
        driver = set_up_browser
        driver.get('https://349skk.csb.app/demo/RadioButtonDemo.html')
        driver.find_element(By.CSS_SELECTOR, '[for="A"]').click()
        pass

    def test_modal(self, set_up_browser):  # открытие модального(диалогового) окна
        driver = set_up_browser
        driver.get('https://ghw76z.csb.app/demo/ConfirmDialogDemo.html')
        driver.find_element(By.XPATH, '(//button/span[contains(text(), "Confirm")])[2]').click()
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Yes"]').click()
        pass

    def test_button_dropdown(self, set_up_browser):  # дропдаун (выпадающий список)
        driver = set_up_browser
        driver.get('https://8sunho.csb.app/demo/SplitButtonDemo.html')
        driver.find_element(By.CSS_SELECTOR, '[aria-owns="pr_id_2_overlay"]').click()
        driver.find_element(By.LINK_TEXT, 'Delete').click()
        pass

    def test_button_calendar(self, set_up_browser):  # календарь
        driver = set_up_browser
        driver.get('https://jpy5dz.csb.app/demo/CalendarDemo.html')
        driver.find_element(By.CSS_SELECTOR, '#range > input').click()
        driver.find_element(By.XPATH, '(//span[contains(text(), "18")])[2]').click()
        driver.find_element(By.XPATH, '(//span[contains(text(), "22")])[2]').click()
        pass