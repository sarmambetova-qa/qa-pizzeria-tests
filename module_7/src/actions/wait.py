import allure
import pytest


@pytest.fixture
def wait_element(page):
    @allure.step('Ожидание элемента со значением {value}')
    def callback(value):
        return page.wait_for_selector(value)
    return callback
