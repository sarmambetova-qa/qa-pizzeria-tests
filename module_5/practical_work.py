import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestValidate:
    def test_keys1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(3)
        el = driver.find_element(By.ID, 'repository-input')
        el.click()
        time.sleep(1)
        el.send_keys(Keys.CONTROL + 'a')
        time.sleep(1)
        el.send_keys(Keys.DELETE)
        time.sleep(1)
        el.send_keys('in:title bug' + Keys.ENTER)
        time.sleep(5)

        issue_titles = driver.find_elements(By.CSS_SELECTOR, 'a[data-hovercard-type="issue"]')
        count = 0
        for title in issue_titles:
            count += 1
        assert count > 0
        print("Найдено задач: ", count)

        for title_element in issue_titles:
            title_text = title_element.text.lower()
            if 'bug' not in title_text:
                print('В названии нет слова "bug":', title_element.text)
                assert False
        print("Тест успешно пройден!")
        pass

    def test_keys2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[contains(text(), "Author")]').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter authors"]').send_keys('bpasero')
        time.sleep(3)
        driver.find_element(By.XPATH, '//span[contains(text(), "bpasero")]').click()
        time.sleep(5)

        issue_titles = driver.find_elements(By.CSS_SELECTOR, 'a[data-hovercard-type="issue"]')
        count = 0
        for title in issue_titles:
            count += 1
        assert count > 0
        print("Найдено задач: ", count)

        author_elements = driver.find_elements(By.CSS_SELECTOR, '.IssueItem-module__authorCreatedLink__YQP27')
        for author in author_elements:
            author_name = author.text.lower()
            if 'bpasero' not in author_name:
                print("Найден автор с другим именем:", author.text)
                assert False
        pass

    def test_keys3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        time.sleep(3)
        driver.find_element(By.ID, 'search_language').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//option[text()="Python"]').click()
        time.sleep(1)
        driver.find_element(By.ID, 'search_stars').send_keys('>20000')
        time.sleep(1)
        driver.find_element(By.ID, 'search_filename').send_keys('environment.yml')
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[contains(text(), "Search")]').click()
        time.sleep(5)

        star_elements = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label*="stars"]')
        count = 0
        for star in star_elements:
            count += 1
        assert count > 0
        print("Найдено репозиториев: ", count)

        for star_element in star_elements:
            star_text = star_element.get_attribute('aria-label')
            star_number = int(star_text.replace('stars', '').strip())
            print("Звёзд:", star_number)
            if star_number <= 20000:
                print("Ошибка! Количество найденных звёзд: ", star_number, "меньше 20000")
                assert False
        pass

    def test_keys4(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/?type=profession')
        time.sleep(5)
        profession_tab = (driver.find_element(By.XPATH, '//span[contains(text(), "Профессия")]'))
        profession_tab.click()
        time.sleep(1)
        profession_tab.click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//span[contains(text(), "Длительность")]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//li[contains(text(), "От 6 до 12 мес.")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text(), "Тематика")]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//li[contains(text(), "API")]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[contains(text(), "Применить")]').click()
        time.sleep(3)

        duration_elements = driver.find_elements(By.XPATH, '//li[contains(text(), "месяц")]')
        count = 0
        for el in duration_elements:
            count += 1
            duration_text = el.text
            print("Найдена длительность: ", duration_text)
        assert count > 0
        print("Найдено курсов: ", count)
        pass

    def test_keys5(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        time.sleep(5)
        points = driver.find_elements(By.CSS_SELECTOR, '.highcharts-point')
        point_found = False

        for point in points:
            aria = point.get_attribute('aria-label')
            if aria and "Nov" in aria:
                action_chains = ActionChains(driver)
                action_chains.move_to_element(point).perform()
                point_found = True
                break
        if not point_found:
            print("Ошибка! Точка за November не найдена")
            assert False
        time.sleep(5)

        tooltips = driver.find_elements(By.CSS_SELECTOR, '.highcharts-tooltip')
        tooltip_found = False
        for tip in tooltips:
            if tip.is_displayed():
                tooltip_found = True
                break
        if tooltip_found:
            print("Тултип отобразился на странице")
        else:
            print("Ошибка! Тултип не отобразился")
            assert False
        pass


