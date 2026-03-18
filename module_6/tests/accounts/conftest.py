import pytest


@pytest.fixture()
def go_to_github(selenium):
    selenium.get('https://github.com')


@pytest.fixture()
def new_fixture():
    pass
