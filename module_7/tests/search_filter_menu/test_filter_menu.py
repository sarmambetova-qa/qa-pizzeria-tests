import pytest
import allure


class TestFilterMenu:
    @pytest.mark.parametrize('profession_name, filter_names', [
        ("Программирование", ["Бэкенд-разработка", "Веб-разработка", "Анализ данных", "IT-инфраструктура", "Остальное"]),
        ("Дизайн", ["Цифровой дизайн", "Дизайн среды", "Мода и фотография", "Остальное"]),
        ("Маркетинг", ["Бренд-маркетинг", "Перформанс-маркетинг", "Электронная коммерция", "Остальное"]),
    ])
    def test_list_filter_block(self, profession_name, filter_names, go_to_url, wait_element, page):
        """
        Тест кейс №3

        Входные данные:
        [
            ["Программирование", ["Бэкенд-разработка", "Веб-разработка", "Анализ данных","IT-инфраструктура", "Остальное"]],
            ["Дизайн", ["Цифровой дизайн", "Дизайн среды", "Мода и фотография", "Остальное"]],
            ["Маркетинг", ["Бренд-маркетинг", "Перформанс-маркетинг", "Электронная коммерция", "Остальное"]],
        ]

        Шаги:
        - Перейти на сайт https://skillbox.ru/courses/?type=profession
        - Нажать на кнопку из массива данных

        Ожидаемые результаты:
        - Проверить, что в левой части фильтра находятся кнопки-фильтры конкретной профессии из списка
        """
        go_to_url('https://skillbox.ru/courses/?type=profession')

        with allure.step(f'Выбор фильтра курсов {profession_name}'):
            wait_element(f"text={profession_name}").click()

        filter_blocks = page.query_selector_all('.programs-filter-directions__sublist--active > li')

        with allure.step('Проверка кнопок фильтрации'):
            for actual_filter, expected_filter in zip(filter_blocks, filter_names):
                with allure.step(f'Сравнение текущего текста "{actual_filter.inner_text()}" с ожидаемым {expected_filter}'):
                    assert actual_filter.inner_text() == expected_filter

        # assert True
