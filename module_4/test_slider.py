from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestSlider:
    def test_slider(self, set_up_browser):  # слайдер (вправо/влево, вверх/вниз)
        driver = set_up_browser
        driver.get('https://xvssqf.csb.app/demo/SliderDemo.html')
        el = driver.find_element(By.XPATH, '(//*[contains(@class, "p-slider-handle")])[4]')  #div вместо * после //
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(el) # нажимает и удерживает элемент
        action_chains.move_by_offset(xoffset=-50, yoffset=0)   #перемещает курсор на 50 вправо по x, 0 по y; -50 влево по х, 0 по у
        action_chains.perform() #выполняет все действия
        action_chains.release().perform()


    def test_splitter(self, set_up_browser):  # сплиттер (вправо/влево, вверх/вниз)
        driver = set_up_browser
        driver.get('https://rzb0if.csb.app/demo/SplitterDemo.html')
        el = driver.find_element(By.XPATH, '(//*[@class="p-slider-handle"])[1]')  #div вместо * после //
        action_chains = webdriver.ActionChains(driver)
        action_chains\
            .click_and_hold(el)\
            .move_by_offset(xoffset=-350, yoffset=0)\
            .perform()
        action_chains.release().perform()

    def test_switch(self, set_up_browser):  # свич (вкл/выкл)
        driver = set_up_browser
        driver.get('https://hrkdkc.csb.app/demo/InputSwitchDemo.html')
        el = driver.find_element(By.XPATH, '(//span)[2]').click()  # div вместо * после //
        pass