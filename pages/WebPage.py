from selenium import webdriver

class WebPage(object):


    def __init__(self, web_driver: webdriver, url=''):
        self.web_driver = web_driver
        if(url!=''):
            self.web_driver.get(url)

