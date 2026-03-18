import allure
import pytest

class AccountsBase:

    @pytest.fixture()
    def go_to_github(self, selenium):
        with allure.step("Открытие страницы http://github.com"):
            selenium.get("http://github.com")




