from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self,app):
        self.app = app


    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/edit.php")):
            driver.find_element(By.LINK_TEXT, "add new").click()

    def open_contacts_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home").click()

    def add_contact(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

        # Birthday
        self.change_select_value("bday",contact.birth_day)
        self.change_select_value("bmonth", contact.birth_month)
        self.change_field_value("byear",contact.birth_year)

        # Anniversary
        self.change_select_value("aday", contact.anniversary_day)
        self.change_select_value("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)

        self.change_field_value("address2", contact.sec_address)
        self.change_field_value("phone2", contact.sec_home)
        self.change_field_value("notes", contact.sec_notes)


    def return_to_home_page(self):
        driver = self.app.driver
        # return to groups page
        driver.find_element(By.LINK_TEXT, "home page").click()

    def test_edit_contact(self, contact):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH,"//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        driver.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()

    def test_delete_contact(self):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.XPATH,"//img[@title='Edit']").click()
        driver.find_element(By.XPATH, "//input[@value='Delete']").click()


    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def change_select_value(self, select_name, text):
        driver = self.app.driver
        if text is not None:
            select_day = Select(driver.find_element(By.NAME, select_name))
            select_day.select_by_value(text)

    def count(self):
        driver = self.app.driver
        self.open_contacts_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        driver = self.app.driver
        self.open_contacts_page()
        contacts = []
        for element in driver.find_elements(By.XPATH, "//tr[@name='entry']"):
            last_name = element.find_element(By.XPATH, ".//td[2]").text
            print("last_name "+last_name)
            first_name = element.find_element(By.XPATH, ".//td[3]").text
            print("first_name "+first_name)
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            print("id "+id)
            contacts.append(Contact(first_name=first_name,last_name=last_name,id=id))
        return contacts








