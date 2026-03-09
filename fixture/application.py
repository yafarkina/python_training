from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper


class Application:
    def __init__(self):
        #self.wd = WebDriver(executable_path="../drivers/geckodriver.exe")
        self.wd = WebDriver(executable_path="C:\PythonProject\drivers\geckodriver.exe")
       # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session= SessionHelper(self)


    def return_to_group_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        wd = self.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.wd
        # open contact page
        wd.find_element_by_link_text("add new").click()

    def ctreate_group(self, group):
        wd = self.wd
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
