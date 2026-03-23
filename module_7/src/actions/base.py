import allure
import pytest


@pytest.fixture
def go_to_url(page):
    @allure.step('Открытие страницы {url}')
    def callback(url):
        page.goto(url, wait_until='domcontentloaded')
    return callback

