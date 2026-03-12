import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestInput:
    def test_keys1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search or jump to…"]').click()
        time.sleep(3)
        el = driver.find_element(By.ID, 'query-builder-test')
        el.clear()
        el.send_keys('in:title bug' + Keys.ENTER)
        time.sleep(5)
        pass

    def test_keys2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[contains(text(), "Author")]').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter authors"]').send_keys('bpasero')
        time.sleep(3)
        driver.find_element(By.XPATH, '//span[contains(text(), "bpasero")]').click()
        time.sleep(5)
        pass

    def test_keys3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        time.sleep(3)
        driver.find_element(By.ID, 'search_language').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//option[text()="Python"]').click()
        time.sleep(1)
        driver.find_element(By.ID, 'search_stars').send_keys('>20000')
        time.sleep(1)
        driver.find_element(By.ID, 'search_filename').send_keys('environment.yml')
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[contains(text(), "Search")]').click()
        time.sleep(5)
        pass

    def test_keys4(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/?type=profession')
        time.sleep(7)
        driver.find_element(By.XPATH, '//span[contains(text(), "Профессия")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text(), "Длительность")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//li[contains(text(), "От 6 до 12 мес.")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text(), "Тематика")]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//li[contains(text(), "API")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[contains(text(), "Применить")]').click()
        time.sleep(5)


    def test_keys5(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        time.sleep(5)
        points = driver.find_elements(By.CSS_SELECTOR, '.highcharts-point')
        for point in points:
            aria = point.get_attribute('aria-label')
            if aria and "Nov" in aria:
                action_chains = webdriver.ActionChains(driver)
                action_chains.move_to_element(point).perform()
                break
        time.sleep(5)









