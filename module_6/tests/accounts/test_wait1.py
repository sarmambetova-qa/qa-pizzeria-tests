import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from module_6.src.actions.components.forms import fill_forms
from module_6.src.helpers.accounts_base import AccountsBase
import logging


logger = logging.getLogger(__name__)


@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestWait(AccountsBase):
    @allure.title('Проверка загрузки страницы')
    def test_wait_page_load(self, selenium, go_to_github):
        logger.info("Test wait_page_load started")
        with allure.step('Ожидание сообщения "The future of building"'):
            selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')

    def test_wait_types(self, selenium, go_to_github):
        # selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        WebDriverWait(selenium, timeout=10).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        )

    def test_wait_dialog(self, selenium):
        with allure.step('Открытие страницы https://m1vcki.csb.app/'):
            selenium.get('https://m1vcki.csb.app/')

        with allure.step('Ожидание отображения формы'):
            WebDriverWait(selenium, timeout=60).until(lambda d: d.find_element(By.ID, "name"))

        fill_forms(selenium, name="awesome_skillbox")

        # selenium.find_element(By.XPATH, '//*[contains(text(), "The future of building")]')
        with allure.step('Ожидание отображения диалогового окна'):
            WebDriverWait(selenium, timeout=5).until(
                lambda d: d.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]')
            )

        with allure.step('Клик по кнопке Ok'):
            selenium.find_element(By.XPATH, '//button/span[contains(text(), "Ok")]').click()

    def test_wait_dialog2(self, selenium):
        with allure.step('Открытие страницы selenium.dev'):
            selenium.get('https://www.selenium.dev/selenium/web/web-form.html')

        with allure.step('Ожидание поля ввода'):
            wait = WebDriverWait(selenium, timeout=10)
            wait.until(lambda d: d.find_element(By.NAME, "my-text"))

        with allure.step('Заполнение формы данными'):
            with allure.step('Заполнение формы'):
                selenium.find_element(By.NAME, "my-text").send_keys("awesome_skillbox")
                selenium.find_element(By.NAME, "my-password").send_keys("123456")
                selenium.find_element(By.CSS_SELECTOR, "textarea").send_keys("Allure test")

            with allure.step('Изменение фокуса'):
                selenium.execute_script('document.activeElement.blur()')

            with allure.step('Завершение заполнения формы'):
                logging.info('Finish fill')

        with allure.step('Отправка формы'):
            selenium.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
