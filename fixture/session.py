from selenium.webdriver.common.by import By

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

