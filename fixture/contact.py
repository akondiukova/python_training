from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        self.contact_cache = None

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

    def test_edit_first_contact(self, contact):
        self.test_edit_contact_by_index(0)

    def test_edit_contact_by_id(self, id, contact):
        driver = self.app.driver
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        driver.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def test_edit_contact_by_index(self, index, contact):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        driver.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def test_delete_contact(self):
        self.test_delete_contact_by_index(0)


    def test_delete_contact_by_index(self,index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None


    def test_delete_contact_by_id(self,id):
        driver = self.app.driver
        self.open_contact_to_edit_by_id(id)
        driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contacts_page()
            self.contact_cache = []
            for element in driver.find_elements(By.XPATH, "//tr[@name='entry']"):
                last_name = element.find_element(By.XPATH, ".//td[2]").text
                first_name = element.find_element(By.XPATH, ".//td[3]").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                address = element.find_element(By.XPATH, ".//td[4]").text
                # allphones = element.find_element(By.XPATH, ".//td[6]").text.splitlines()
                allphones = element.find_element(By.XPATH, ".//td[6]").text
                # self.contact_cache.append(Contact(first_name=first_name,last_name=last_name,id=id,home_phone=allphones[0],
                #                                   mobile_phone=allphones[1],work_phone=allphones[2]))
                allemails = element.find_element(By.XPATH, ".//td[5]").text
                self.contact_cache.append(
                    Contact(first_name=first_name, last_name=last_name, id=id,
                            all_phones_from_home_page=allphones, address=address, all_emails = allemails))
        return list(self.contact_cache)

    def get_contact_info_by_id(self, id):
        driver = self.app.driver
        self.open_contacts_page()
        self.contact_cache = []
        contact = driver.find_element(By.CSS_SELECTOR, "tr[name='entry']:has(input[id='%s'])" % id)
        last_name = contact.find_element(By.XPATH, ".//td[2]").text
        first_name = contact.find_element(By.XPATH, ".//td[3]").text
        address = contact.find_element(By.XPATH, ".//td[4]").text
        allphones = contact.find_element(By.XPATH, ".//td[6]").text
        allemails = contact.find_element(By.XPATH, ".//td[5]").text
        return Contact(first_name=first_name, last_name=last_name, id=id,
                    all_phones_from_home_page=allphones, address=address, all_emails=allemails)


    def open_contact_to_view_by_index(self, index):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_elements(By.NAME, "selected[]")[index].click()
        driver.find_elements(By.XPATH, "//img[@title='Details']")[index].click()

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_elements(By.NAME, "selected[]")[index].click()
        driver.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()


    def open_contact_to_edit_by_id(self, id):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element(By.CSS_SELECTOR, "input[id='%s']" % id).click()
        driver.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = driver.find_element(By.NAME, "id").get_attribute("value")
        address = driver.find_element(By.NAME, "address").get_attribute("value")
        homephone = driver.find_element(By.NAME,"home").get_attribute("value")
        workphone = driver.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = driver.find_element(By.NAME, "mobile").get_attribute("value")
        secphone = driver.find_element(By.NAME, "phone2").get_attribute("value")

        email1 = driver.find_element(By.NAME, "email").get_attribute("value")
        email2 = driver.find_element(By.NAME, "email2").get_attribute("value")
        email3 = driver.find_element(By.NAME, "email3").get_attribute("value")

        return Contact(first_name=firstname,last_name=lastname,home_phone=homephone,mobile_phone=mobilephone,
                       work_phone=workphone,id=id,sec_home=secphone,address=address, email = email1, email2 = email2, email3 = email3)


    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_to_view_by_index(index)
        text = driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)",text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone)


    def add_contact_in_group_by_id(self, id_contact, id_group):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element(By.CSS_SELECTOR, "input[id='%s']" % id_contact).click()
        select_group = Select(driver.find_element(By.NAME, "to_group"))
        select_group.select_by_value('%s' % id_group)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def delete_contact_from_group_by_id(self, id_contact, id_group):
        driver = self.app.driver
        self.open_contacts_page()
        select_group = Select(driver.find_element(By.NAME, "group"))
        select_group.select_by_value('%s' % id_group)
        driver.find_element(By.CSS_SELECTOR, "input[id='%s']" % id_contact).click()
        driver.find_element(By.XPATH, "//input[@name='remove']").click()











