from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://yandex.ru/")

    #проверка наличия поля поиска
    assert "input__input" in driver.page_source

    imputBox = driver.find_element_by_class_name("input__input")
    imputBox.click()
    imputBox.send_keys("тензор")
    #imputBox.send_keys(Keys.ENTER)

    #проверка появления таблицы с подсказками
    manual_focus = driver.find_elements_by_class_name("search2_manual-focus_yes")
    assert len(manual_focus)==1

    #провкрка на содержание в результате поиска ссысок на tenzor.ru
    imputBox.send_keys(Keys.ENTER)
    #desktop-card
    #serp_item = driver.find_element_by_class_name("serp-item")
    #i_bem = driver.find_elements_by_css_selector("li.serp-item")
    #i_bem = driver.find_elements_by_css_selector("a.organic__url")
    #i_bem=driver.find_elements_by_xpath("//a[@class='organic__url']/dl/dd")

    i_bem = driver.find_elements_by_css_selector("a.organic__url")
    assert sum( int(1) for x in i_bem if x.get_attribute("href") == "https://tensor.ru/") == 1
    for i in i_bem:
        print(i.get_attribute("href"))

    imputBox.click()
    # button = driver.find_element_by_class_name("search2__button")
    # button.click()

def images():
    driver = webdriver.Chrome()
    driver.get("https://yandex.ru/")

    #image button exists
    assert "images" in driver.page_source
    images = driver.find_element_by_xpath("//a[@data-id='images']")
    images.click()

    #current url is https://yandex.ru/images
    driver.switch_to.window(driver.window_handles[1])
    assert "https://yandex.ru/images/" in str(driver.current_url)
    #after openning 1 category it's text right
    images = driver.find_element_by_class_name("PopularRequestList-Preview")
    text = images.text
    time.sleep(2)
    images.click()
    current_page_input_text=driver.find_element_by_class_name("input__control").get_attribute("value")
    assert current_page_input_text == text
    #check openning image
    time.sleep(2)
    #i = driver.find_element_by_xpath("//div[@class='serp-item__preview']/div/div[@class='polaroid2__content']/div[@class='polaroid2__wrapper']/div[@class='polaroid2__title']")
    img = driver.find_element_by_xpath("//div[@class='serp-item__preview']")
    ActionChains(driver).move_to_element(img).perform()
    time.sleep(2)
    ActionChains(driver).move_to_element(img).perform()
    time.sleep(2)
    i=img.find_element_by_class_name('polaroid2__title').get_attribute("innerHTML")

    #images =driver.find_element_by_class_name("polaroid2_with-actions")
    #img=images.g.find_element_by_class_name("polaroid2__title")
    images =driver.find_element_by_class_name("serp-item__preview")
    images.click()
    time.sleep(2)
    i2= driver.find_element_by_class_name("MMOrganicSnippet-Text").get_attribute("innerHTML")
    assert i in i2
    #chek img changing
    src = driver.find_element_by_class_name("MMImage-Origin").get_attribute("src")
    driver.find_element_by_class_name("CircleButton_type_next").click()
    src2 = driver.find_element_by_class_name("MMImage-Origin").get_attribute("src")
    assert src2 != src
    driver.find_element_by_class_name("CircleButton_type_prev").click()
    assert src == driver.find_element_by_class_name("MMImage-Origin").get_attribute("src")

    images.click()


if __name__ == '__main__':
    #main()
    images()