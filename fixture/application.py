from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        #self.wd = WebDriver(executable_path="../drivers/geckodriver.exe")
        self.wd = WebDriver(executable_path="C:\PythonProject\drivers\geckodriver.exe")
       # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session= SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)



    def destroy(self):
        self.wd.quit()
