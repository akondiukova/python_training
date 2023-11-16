# -*- coding: utf-8 -*-
from _pytest import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import unittest
from group import Group

class AddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.auth(driver, "admin", "secret")
        self.open_groups_page(driver)
        self.add_group(driver,Group ("1","2","3"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.auth(driver, "admin", "secret")
        self.open_groups_page(driver)
        self.add_group(driver, Group ("", "", ""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def auth(self,driver,usarname,password):
        field_name = driver.find_element("name", "user")
        field_name.send_keys(usarname)
        field_pas = driver.find_element("name", "pass")
        field_pas.send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self, driver):
        driver.find_element(By.ID, "header").click()
        driver.find_element(By.LINK_TEXT, "groups").click()

    def add_group(self,driver,group):
        # init group creation
        driver.find_element(By.NAME,"new").click()
        # fill group form
        driver.find_element(By.NAME,"group_name").send_keys(group.name)
        driver.find_element(By.NAME,"group_header").send_keys(group.header)
        driver.find_element(By.NAME,"group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME,"submit").click()

    def return_to_groups_page(self, driver):
        # return to groups page
        driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()