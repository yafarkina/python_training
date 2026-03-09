from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        #self.wd = WebDriver(executable_path="../drivers/geckodriver.exe")
        self.wd = WebDriver(executable_path="C:\PythonProject\drivers\geckodriver.exe")
       # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session= SessionHelper(self)
        self.group = GroupHelper(self)

    def return_to_home_page(self):
        wd = self.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.wd
        # open contact page
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
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


    def destroy(self):
        self.wd.quit()
