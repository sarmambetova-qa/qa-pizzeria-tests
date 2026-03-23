import pytest
import time
import allure


class TestCountProfessions:
    @pytest.fixture
    def setup_count_profession_test(self, go_to_url, wait_element, page):
        go_to_url('https://skillbox.ru/courses/')
        time.sleep(3)

        with allure.step('Нажатие на вкладку "Профессия"'):
            wait_element('//span[contains(text(), "Профессия")]').click(force=True)

        # Проверяем URL, так как иногда клик не срабатывает
        if 'type=profession' not in page.url:
            page.goto('https://skillbox.ru/courses/?type=profession', wait_until='domcontentloaded')
            time.sleep(3)

        return wait_element('.programs-gallery > .programs-gallery__load')


    def test_default_count(self, setup_count_profession_test):
        """
        Тест кейс №1:

        Шаги:
        - Перейти на сайт https://skillbox.ru/courses/
        - Найти и кликнуть по вкладке "Профессия"
        - Запомнить количество отображаемых профессий (программ) - 178
        - Найти кнопку "Ещё 12 программ из 166"

        Ожидаемые результаты:
        - В кнопке после профессий отображается надпись "Ещё 12 программ из 166"
        """
        # selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        actual_text = setup_count_profession_test.inner_text()
        expected_text = 'Ещё 12 программ из 166'

        with allure.step(f'Проверка, что в кнопке загрузки содержится текст "{expected_text}"'):
            assert expected_text in actual_text

    def test_count_after_load_additional_professions(self, setup_count_profession_test, wait_element, page):
        """
        Тест кейс №2

        Шаги:
        - Перейти на сайт https://skillbox.ru/courses/
        - Найти и кликнуть по вкладке "Профессия"
        - Запомнить количество отображаемых профессий (программ) - 178
        - Нажать на кнопку "Ещё 12 программ из 166"

        Ожидаемые результаты:
        - Проверить, что добавились новые блоки
        - Кнопка после профессий отображает текст "Ещё 12 программ из 154"
        """
        default_count_button = setup_count_profession_test
        expected_text = 'Ещё 12 программ из 154'
        with allure.step('Загрузка второй страницы'):
            default_count_button.click()
            time.sleep(3)

        assert expected_text in wait_element('.programs-gallery > .programs-gallery__load').inner_text()
