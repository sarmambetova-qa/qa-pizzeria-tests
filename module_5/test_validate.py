import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_attribute_to_include


class TestValidate:
    def test_is_selected(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://m1vcki.csb.app/')
        time.sleep(10)

        name_field = driver.find_element(By.ID, 'name')
        expected_value = 'skillbox'
        name_field.send_keys(expected_value)

        assert name_field.get_attribute('value') == expected_value
        pass


    def test_checkbox(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://mkunc5.csb.app/')
        checkbox = driver.find_element(By.CSS_SELECTOR, 'input')
        checkbox.click()

        assert checkbox.is_selected() is True
        pass


    def test_button(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://f05jq8.csb.app/demo/ButtonDemo.html')

        assert element_attribute_to_include(
            locator=(By.CSS_SELECTOR, '[aria-label="Disabled"]'),
            attribute_='disabled'
        )(driver) is True
        pass
