#  -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(executable_path="drivers/geckodriver.exe")
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password= "secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact(firstname = "first", lastname = "last", company = "company", address = "address", telephone = "home"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd: WebDriver):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd: WebDriver):
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd: WebDriver, contact):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.telephone)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def open_contact_page(self, wd: WebDriver):
        # open contact page
        wd.find_element_by_link_text("add new").click()

    def login(self, wd: WebDriver, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd: WebDriver):
        # open home page
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()






