#  -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(executable_path="drivers/geckodriver.exe")
        #self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username = "admin", password = "secret")
        self.ctreate_group(wd, Group(name = "test", header = "test", footer = "test"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username = "admin", password = "secret")
        self.ctreate_group(wd, Group( name = "", header = "", footer = ""))
        self.logout(wd)

    def logout(self, wd: WebDriver):
        # return to groups page
        wd.find_element_by_link_text("group page").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

    def ctreate_group(self, wd: WebDriver, group):
        # init group creation
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def login(self, wd: WebDriver, username, password):
        # open home page
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
