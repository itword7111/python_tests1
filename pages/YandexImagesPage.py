from selenium import webdriver
from pages.WebPage import WebPage


class YandexImagesPage(WebPage):

    def __init__(self, web_driver: webdriver):
        WebPage.__init__(self, web_driver)
        self.imageCategory = self.web_driver.find_element_by_class_name("PopularRequestList-Preview")
        self.current_page_input = self.web_driver.find_element_by_class_name("input__control")

    def getImageOfCategory(self):
        return self.web_driver.find_element_by_xpath("//div[@class='serp-item__preview']")

    def getFocusedImgText(self):
        return self.getImageOfCategory().find_element_by_class_name('polaroid2__title').get_attribute("innerHTML")

    def getChousenImgText(self):
        return self.web_driver.find_element_by_class_name("MMOrganicSnippet-Text").get_attribute("innerHTML")

    def getChousenImg(self):
        return self.web_driver.find_element_by_class_name("MMImage-Origin").get_attribute("src")

    def findNextImg(self):
        self.web_driver.find_element_by_class_name("CircleButton_type_next").click()

    def findPreviousImg(self):
        self.web_driver.find_element_by_class_name("CircleButton_type_prev").click()
