from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements(By.NAME, "new")) > 0):
            driver.find_element(By.ID, "header").click()
            driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # init group creation
        driver.find_element(By.NAME,"new").click()
        self.fill_group_form(group)
        # submit group creation
        driver.find_element(By.NAME,"submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    def return_to_groups_page(self):
        driver = self.app.driver
        # return to groups page
        driver.find_element(By.LINK_TEXT, "group page").click()

    def test_delete_first_group(self):
        self.test_delete_group_by_index(0)

    def test_delete_group_by_index(self,index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def test_mofify_first_group(self):
       self.test_mofify_group_by_index(0)


    def test_mofify_group_by_index(self,index, group):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self,index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
           driver = self.app.driver
           self.open_groups_page()
           self.group_cache = []
           for element in driver.find_elements(By.CSS_SELECTOR, "span.group"):
               text = element.text
               id = element.find_element(By.NAME, "selected[]").get_attribute("value")
               self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)

    def test_delete_group_by_id(self,id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def test_mofify_group_by_id(self,group,id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self,id):
        driver = self.app.driver
        driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()


