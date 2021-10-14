from selenium import webdriver
from pages.WebPage import WebPage


class YandexSearchPage(WebPage):

    def __init__(self, web_driver: webdriver):
        WebPage.__init__(self, web_driver)
        self.results = self.web_driver.find_elements_by_css_selector("a.organic__url")

    def update(self):
        self.results = self.web_driver.find_elements_by_css_selector("a.organic__url")
