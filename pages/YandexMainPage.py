from selenium import webdriver
from pages.WebPage import WebPage
from pages.YandexSearchPage import YandexSearchPage
from pages.YandexImagesPage import YandexImagesPage
from selenium.webdriver.common.keys import Keys
import copy


class YandexMainPage(WebPage):

    def __init__(self, web_driver: webdriver):
        WebPage.__init__(self, web_driver, "https://yandex.ru/")
        self.imputBox = self.web_driver.find_element_by_class_name("input__input")
        self.manual_focus = self.web_driver.find_elements_by_class_name("search2_manual-focus_yes")
        self.images_button = self.web_driver.find_element_by_xpath("//a[@data-id='images']")

    def update(self):
        self.manual_focus = self.web_driver.find_elements_by_class_name("search2_manual-focus_yes")

    def submitSearch(self):
        self.imputBox.send_keys(Keys.ENTER)
        return YandexSearchPage(self.web_driver)

    def imageButtonClick(self):
        self.images_button.click()
        self.web_driver.switch_to.window(self.web_driver.window_handles[1])
        return YandexImagesPage(self.web_driver)
