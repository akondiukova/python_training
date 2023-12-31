from selenium import webdriver
import pytest
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application():

    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognize browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl = baseUrl


    def open_home_page(self):
        driver = self.driver
        driver.get(self.baseUrl)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
       self.driver.quit()

