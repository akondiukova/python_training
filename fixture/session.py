from selenium.webdriver.common.by import By
import time

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def auth(self,usarname,password):
        driver = self.app.driver
        self.app.open_home_page()
        field_name = driver.find_element("name", "user")
        field_name.send_keys(usarname)
        field_pas = driver.find_element("name", "pass")
        field_pas.send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(1)


    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self,usarname):
        driver = self.app.driver
        return self.get_logged_user() == usarname

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def ensure_auth(self,usarname,password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(usarname):
                return
            else:
                self.logout()
        self.auth(usarname,password)





