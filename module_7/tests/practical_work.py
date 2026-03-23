import allure
import time

class TestValidate:
    def test_keys1(self, go_to_url, wait_element, page):
        go_to_url('https://github.com/microsoft/vscode/issues')
        time.sleep(1)

        with allure.step('Найти поле поиска и очистить его'):
            el = wait_element('#repository-input')
            el.click()
            el.press('Control+a')
            el.press('Delete')
            time.sleep(1)

        with allure.step('Ввести фильтр "in:title bug" и выполнить поиск'):
            el.fill('in:title bug')
            el.press('Enter')
            time.sleep(2)

        with allure.step('Ожидаем загрузки результатов'):
            wait_element('a[data-hovercard-type="issue"]')
            time.sleep(1)

        with allure.step('Получить все названия задач'):
            issue_titles = page.locator('a[data-hovercard-type="issue"]').all()
            count = 0
            for title in issue_titles:
                count += 1
            print("Найдено задач: ", count)

        with allure.step(f'Проверка, что найдены задачи'):
            assert count > 0

        with allure.step('Проверка, что все задачи содержат слово "bug" в названии'):
            for title_element in issue_titles:
                title_text = title_element.inner_text().lower()
                if 'bug' not in title_text:
                    print('В названии нет слова "bug":', title_element.inner_text())
                    assert False

        print("Тест успешно пройден!")

    def test_keys2(self, go_to_url, wait_element, page):
        go_to_url('https://github.com/microsoft/vscode/issues')
        time.sleep(1)

        with allure.step('Нажать на кнопку Author'):
            wait_element('//*[contains(text(), "Author")]').click()
            time.sleep(1)

        with allure.step('Ввести в поиск имя bpasero'):
            wait_element('input[placeholder="Filter authors"]').fill('bpasero')
            time.sleep(1)

        with allure.step('Дождаться появления и выбрать автора bpasero'):
            wait_element('//span[contains(text(), "bpasero")]').click()
            time.sleep(2)

        with allure.step('Ожидаем загрузки результатов'):
            wait_element('a[data-hovercard-type="issue"]')
            time.sleep(1)

        with allure.step('Получить все названия задач'):
            issue_titles = page.locator('a[data-hovercard-type="issue"]').all()
            count = 0
            for title in issue_titles:
                count += 1
            print("Найдено задач: ", count)

        with allure.step('Проверка, что найдены задачи'):
            assert count > 0

        with allure.step('Проверка, что автор всех задач bpasero'):
            author_elements = page.locator('.IssueItem-module__authorCreatedLink__YQP27').all()
            for author in author_elements:
                author_name = author.inner_text().lower()
                if 'bpasero' not in author_name:
                    print("Найден автор с другим именем:", author.inner_text())
                    assert False
        print("Тест успешно пройден!")

    def test_keys3(self, go_to_url, wait_element, page):
        go_to_url('https://github.com/search/advanced')
        time.sleep(1)

        with allure.step('Выбрать язык Python'):
            page.select_option('#search_language', 'Python')
            time.sleep(1)

        with allure.step('Ввести количество звёзд >20000'):
            wait_element('#search_stars').fill('>20000')
            time.sleep(1)

        with allure.step('Ввести название файла environment.yml'):
            wait_element('#search_filename').fill('environment.yml')
            time.sleep(1)

        with allure.step('Нажать на кнопку поиска'):
            wait_element('//button[contains(text(), "Search")]').click()
            time.sleep(3)

        with allure.step('Ожидаем загрузки результатов'):
            wait_element('a[aria-label*="stars"]')
            time.sleep(1)

        with allure.step('Получить все репозитории'):
            star_elements = page.locator('a[aria-label*="stars"]').all()
            count = 0
            for star in star_elements:
                count += 1
            print("Найдено репозиториев: ", count)

        with allure.step('Проверка, что найдены репозитории'):
            assert count > 0

        with allure.step('Проверка, что количество звёзд >20000'):
            for star_element in star_elements:
                star_text = star_element.get_attribute('aria-label')
                star_number = int(star_text.replace('stars', '').strip())
                print("Звёзд:", star_number)
                if star_number <= 20000:
                    print("Ошибка! Количество найденных звёзд: ", star_number, "меньше 20000")
                    assert False

        print("Тест успешно пройден!")

    def test_keys4(self, go_to_url, wait_element, page):
        go_to_url('https://skillbox.ru/code/?type=profession')
        time.sleep(3)

        with allure.step('Выбрать вкладку "Профессия"'):
            profession_tab = wait_element('//span[contains(text(), "Профессия")]')
            profession_tab.click()
            time.sleep(1)
            profession_tab.click()
            time.sleep(2)

        with allure.step('Выбрать длительность "От 6 до 12 мес."'):
            wait_element('//span[contains(text(), "Длительность")]').click()
            time.sleep(1)
            wait_element('//li[contains(text(), "От 6 до 12 мес.")]').click()
            time.sleep(2)

        with allure.step('Выбрать тематику "API"'):
            wait_element('//span[contains(text(), "Тематика")]').click()
            time.sleep(1)
            wait_element('//li[contains(text(), "API")]').click()
            time.sleep(2)

        with allure.step('Нажать кнопку "Применить"'):
            wait_element('//*[contains(text(), "Применить")]').click()
            time.sleep(3)

        with allure.step('Получить все курсы'):
            duration_elements = page.locator('//li[contains(text(), "месяц")]').all()
            count = 0
            for el in duration_elements:
                count += 1
                duration_text = el.inner_text()
                print("Найдена длительность: ", duration_text)

        with allure.step('Проверка, что найдены курсы'):
            assert count > 0
            print("Найдено курсов: ", count)

        print("Тест успешно пройден!")

    def test_keys5(self, go_to_url, wait_element, page):
        go_to_url('https://github.com/microsoft/vscode/graphs/commit-activity')
        time.sleep(8)

        with allure.step('Проверить, что график загрузился'):
            wait_element('.highcharts-container')
            time.sleep(3)

        with allure.step('Найти точки на графике'):
            points = page.locator('.highcharts-point').all()
            point_found = False

        with allure.step('Навести мышку на точку с November'):
            for point in points:
                aria = point.get_attribute('aria-label')
                if aria and "Nov" in aria:
                    point.hover()
                    point_found = True
                    break

        with allure.step('Проверка, что точка November найдена'):
            if not point_found:
                print("Ошибка! Точка за November не найдена")
                assert False

        time.sleep(2)

        with allure.step('Проверить, что тултип отобразился'):
            tooltip = page.locator('.highcharts-tooltip')
            if tooltip.count() > 0:
                print("Тултип отобразился на странице")
            else:
                print("Ошибка! Тултип не отобразился")
                assert False

        print("Тест успешно пройден!")
