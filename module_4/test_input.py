from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestInput:
    def test_send_keys(self, set_up_browser):   # ввод значений
        driver = set_up_browser
        driver.get('https://l6nm9r.csb.app/demo/InputTextDemo.html')
        driver.find_element(By.ID, 'username1').send_keys('basic text')

    def test_clear(self, set_up_browser):   # очищаем значения
        driver = set_up_browser
        driver.get('https://l6nm9r.csb.app/demo/InputTextDemo.html')
        el = driver.find_element(By.ID, 'username1')
        el.send_keys('basic text')
        el.clear()

    def test_copy_paste(self, set_up_browser):  # копируем значения
        driver = set_up_browser
        driver.get('https://l6nm9r.csb.app/demo/InputTextDemo.html')
        el = driver.find_element(By.ID, 'username1')
        el.send_keys('basic text')

        action_chains = webdriver.ActionChains(driver)   # вставляем значения

        action_chains.key_down(Keys.CONTROL).send_keys('a').perform() # Нажимаем Ctrl + A (выделить всё)
        action_chains.key_down(Keys.CONTROL).send_keys('c').perform()  # Нажимаем Ctrl + C (копировать)
        el.clear()
        el.click()                                         # driver.find_element(By.ID, 'other_field').click() Переходим к другому полю (кликаем на него)
        action_chains.key_down(Keys.CONTROL).send_keys('v').perform()  # Нажимаем Ctrl + V (вставить)

    def test_input_mask(self, set_up_browser):  # вводим цифры в поле, маска
        driver = set_up_browser
        driver.get('https://jbms5d.csb.app/demo/InputMaskDemo.html') # вводим сайт, где есть маска
        el = driver.find_element(By.ID, 'basic')
        value = '12345678'
        for c in value:
            el.send_keys(c)
            time.sleep(0.2)  # ввода цифр с задержкой 200 милисек.

    def test_input_filter(self, set_up_browser):  # фильтр
        driver = set_up_browser
        driver.get('https://vypr70.csb.app/demo/KeyFilterDemo.html')  # стр. сайта, где отображается поле (ввод только буквы)
        driver.find_element(By.ID, 'alpha').send_keys('asd123qwe321')

    def test_input_tag(self, set_up_browser):  # теги
        driver = set_up_browser
        driver.get('https://esy8bz.csb.app/demo/ChipsDemo.html')  # стр. с тегами
        driver.find_element(By.XPATH, '(//input)[3]').send_keys('skillbox' + Keys.ENTER)
        driver.find_element(By.XPATH, '(//input)[3]').send_keys('python' + Keys.ENTER)
        driver.find_element(By.XPATH, '(//input)[3]').send_keys('pytest' + Keys.ENTER)
        pass

