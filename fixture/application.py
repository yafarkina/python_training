from selenium import webdriver

from fixture.contact_in_group import ContactInGroupHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    #def __init__(self, browser="Firefox", base_url = "http://localhost/addressbook/"): #если хотим запускать с параметрами прибитыми гвоздями
    def __init__(self, browser, base_url):         #если хотим запускать указывая параметры из командной строки
      # self.wd = WebDriver(executable_path="../drivers/geckodriver.exe")
       if browser == "Firefox":
           self.wd = webdriver.Firefox(executable_path="C:\PythonProject\drivers\geckodriver.exe")
       elif browser == "Chrome":
            self.wd = webdriver.Chrome(executable_path="C:\PythonProject\drivers\chromedriver.exe")
       elif browser == "Edge":
            self.wd = webdriver.Edge(executable_path="C:\PythonProject\drivers\msedgedriver.exe")
       else :
            raise ValueError("Unsupported browser %s" % browser)
       #   self.wd.implicitly_wait(10)  если требуется поставить ожидание загрузки динамических элементов
       self.session= SessionHelper(self)
       self.group = GroupHelper(self)
       self.contact = ContactHelper(self)
       self.contact_in_group = ContactInGroupHelper(self)
       self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        self.wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
