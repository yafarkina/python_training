from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        # open contact page
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        wd = self.app.wd
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector("img[title=\"Edit\"]")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_fild_value("firstname", contact.firstname)
        self.change_fild_value("lastname", contact.lastname)
        self.change_fild_value("company", contact.company)
        self.change_fild_value("address", contact.address)
        self.change_fild_value("home", contact.telephone)

    def change_fild_value(self, fild_name, fild_value):
        wd = self.app.wd
        if fild_value is not None:
           wd.find_element_by_name(fild_name).click()
           wd.find_element_by_name(fild_name).clear()
           wd.find_element_by_name(fild_name).send_keys(fild_value)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=\"entry\"]"):
            #for element in wd.find_elements_by_css_selector("tr.entry"):
                cell = element.find_elements_by_tag_name("td")
                firstname = cell[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname = firstname, id = id))
        return list(self.contact_cache)