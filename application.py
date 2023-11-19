from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Application():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self,):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def auth(self,usarname,password):
        driver = self.driver
        self.open_home_page()
        field_name = driver.find_element("name", "user")
        field_name.send_keys(usarname)
        field_pas = driver.find_element("name", "pass")
        field_pas.send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.ID, "header").click()
        driver.find_element(By.LINK_TEXT, "groups").click()

    def add_group(self,group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element(By.NAME,"new").click()
        # fill group form
        driver.find_element(By.NAME,"group_name").send_keys(group.name)
        driver.find_element(By.NAME,"group_header").send_keys(group.header)
        driver.find_element(By.NAME,"group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME,"submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        # return to groups page
        driver.find_element(By.LINK_TEXT, "group page").click()

    def open_contact_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def add_contact(self, contact):
        driver = self.driver
        # fill contact form
        self.open_contact_page()
        driver.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        driver.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        driver.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        driver.find_element(By.NAME, "title").send_keys(contact.title)
        driver.find_element(By.NAME, "company").send_keys(contact.company)
        driver.find_element(By.NAME, "address").send_keys(contact.address)
        driver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        driver.find_element(By.NAME, "work").send_keys(contact.work_phone)
        driver.find_element(By.NAME, "email").send_keys(contact.email)
        driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)

        # Birthday
        select_day = Select(driver.find_element(By.NAME, "bday"))
        select_day.select_by_value(contact.birth_day)
        select_month = Select(driver.find_element(By.NAME, "bmonth"))
        select_month.select_by_value(contact.birth_month)
        driver.find_element(By.NAME, "byear").send_keys(contact.birth_year)

        # Anniversary
        select_ann_day = Select(driver.find_element(By.NAME, "aday"))
        select_ann_day.select_by_value(contact.anniversary_day)
        select_ann_month = Select(driver.find_element(By.NAME, "amonth"))
        select_ann_month.select_by_value(contact.anniversary_month)
        driver.find_element(By.NAME, "ayear").send_keys(contact.anniversary_year)

        driver.find_element(By.NAME, "address2").send_keys(contact.sec_address)
        driver.find_element(By.NAME, "phone2").send_keys(contact.sec_home)
        driver.find_element(By.NAME, "notes").send_keys(contact.sec_notes)
        # submit contact creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.driver
        # return to groups page
        driver.find_element(By.LINK_TEXT, "home page").click()


    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        driver = self.driver
        self.driver.quit()

