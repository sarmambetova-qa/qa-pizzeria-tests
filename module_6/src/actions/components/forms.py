import logging
from selenium.webdriver.common.by import By
import allure


@allure.step('Заполнение формы данными')
def fill_forms(selenium, name='skillbox'):
    logging.info('Start fill form')
    with allure.step('Заполнение формы'):
        selenium.find_element(By.ID, 'name').send_keys(name)
        selenium.find_element(By.ID, 'email').send_keys('skillbox@mail.ru')
        selenium.find_element(By.NAME, 'password').send_keys('skillbox')

    with allure.step('Изменение фокуса'):
        selenium.execute_script('document.activeElement.blur()')

    with allure.step('Завершение заполнения формы'):
        selenium.find_element(By.CSS_SELECTOR, '[role="checkbox"]').click()
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Submit")]').click()
    logging.info('Finish fill')
