from unittest import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

from pages.YandexMainPage import YandexMainPage


class TestYandexImagePage(unittest.TestCase):
    def testSearchPage(self):
        mainPage = YandexMainPage(webdriver.Chrome())

        # проверка наличия поля поиска
        self.assertTrue("input__input" in mainPage.web_driver.page_source, "поисковой строки нет")

        imputBox = mainPage.web_driver.find_element_by_class_name("input__input")
        mainPage.imputBox.click()
        mainPage.imputBox.send_keys("тензор")

        # проверка появления таблицы с подсказками
        mainPage.update()
        self.assertTrue(len(mainPage.manual_focus) == 1, "таблицы с подсказками не появилась")

        # провкрка на содержание в результате поиска ссысок на tenzor.ru
        searchPage = mainPage.submitSearch()
        self.assertTrue(
            sum(int(1) for x in range(5) if searchPage.results[x].get_attribute("href") == "https://tensor.ru/") == 5,
            "из первых пяти результатов поиска, не все ссылаются на https://tensor.ru/")

    def testImagesPage(self):
        mainPage = YandexMainPage(webdriver.Chrome())
        # image button exists
        self.assertTrue("images" in mainPage.web_driver.page_source, "нет кнопки картинки")
        # current url is https://yandex.ru/images
        imagesPage = mainPage.imageButtonClick()
        self.assertTrue("https://yandex.ru/images/" in str(imagesPage.web_driver.current_url),
                        "текущая ссылка не https://yandex.ru/images/")
        # after openning 1 category it's text right
        text = imagesPage.imageCategory.text
        time.sleep(2)
        imagesPage.imageCategory.click()
        current_page_input_text = imagesPage.current_page_input.get_attribute("value")
        self.assertTrue(current_page_input_text == text, "выбранная категория не окрылась")
        # check openning image
        time.sleep(2)

        imageOfCategory = imagesPage.getImageOfCategory()

        ActionChains(imagesPage.web_driver).move_to_element(imageOfCategory).perform()
        time.sleep(2)
        ActionChains(imagesPage.web_driver).move_to_element(imageOfCategory).perform()
        time.sleep(2)
        HtmlOfFocusedImg = imagesPage.getFocusedImgText()
        # images =driver.find_element_by_class_name("polaroid2_with-actions")
        # img=images.g.find_element_by_class_name("polaroid2__title")
        images = imagesPage.web_driver.find_element_by_class_name("serp-item__preview")
        images.click()
        time.sleep(2)
        HtmlOfChousenImg = imagesPage.getChousenImgText()
        self.assertTrue(HtmlOfFocusedImg in HtmlOfChousenImg, "выбранная картинка не окрылась")
        # chek img changing
        src = imagesPage.getChousenImg()
        imagesPage.findNextImg()
        src2 = imagesPage.getChousenImg()
        self.assertTrue(src2 != src, "картинка не переключилась")
        imagesPage.findPreviousImg()
        self.assertTrue(src == imagesPage.getChousenImg(), "картинка не переключилась обратно")
