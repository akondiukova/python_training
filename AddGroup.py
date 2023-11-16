# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


import unittest, time, re

class AddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_group(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        self.auth(driver, "admin", "secret")
        driver.find_element(By.ID,"header").click()
        driver.find_element(By.LINK_TEXT,"groups").click()
        self.add_group(driver)
        driver.find_element(By.LINK_TEXT,"group page").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()


    def auth(self,driver,usarname,password):
        field_name = driver.find_element("name", "user")
        field_name.send_keys(usarname)
        field_pas = driver.find_element("name", "pass")
        field_pas.send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()


    def add_group(self,driver):
        driver.find_element(By.NAME,"new").click()
        driver.find_element(By.NAME,"group_name").send_keys("1")
        driver.find_element(By.NAME,"group_header").send_keys("2")
        driver.find_element(By.NAME,"group_footer").send_keys("3")
        driver.find_element(By.NAME,"submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
