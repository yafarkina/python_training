import re
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
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector("img[title=\"Edit\"]")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector("img[title=\"Details\"]")[index].click()

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
        self.change_fild_value("home", contact.homephone)
        self.change_fild_value("mobile", contact.mobilephone)
        self.change_fild_value("work", contact.workphone)
        self.change_fild_value("email", contact.email)
        self.change_fild_value("email2", contact.email2)
        self.change_fild_value("email3", contact.email3)

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                id_ct = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                email = all_emails[0]
                email2 = all_emails[1]
                email3 = all_emails[2]
                self.contact_cache.append(Contact(firstname = firstname,
                                                  id = id_ct,
                                                  lastname=lastname,
                                                  address = address,
                                                  all_phones_from_home_page = all_phones,
                                                  homephone=all_phones[0],
                                                  mobilephone=all_phones[1],
                                                  workphone=all_phones[2],
                                                  email=email,
                                                  email2=email2,
                                                  email3=email3,
                                                  all_emails_from_home_page = all_emails
                                                  ))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id_ct = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname= firstname, lastname= lastname, address=address,
                       id = id_ct, homephone = homephone, workphone = workphone, mobilephone = mobilephone,
                       email = email, email2= email2, email3 = email3
                       )

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        all_ls = re.findall("(.*)", text)
        firstname = all_ls[0].split(" ")[0]
        lastname = all_ls[0].split(" ")[1]
        address = all_ls[4].split(" ")[0]
        homephone= re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        all_emails = re.findall("([\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,})", text)
        email = all_emails[0]
        email2 = all_emails[1]
        email3 = all_emails[2]
        return Contact(
                       firstname=firstname,
                       lastname=lastname,
                       address=address,
                       homephone=homephone,
                       workphone=workphone,
                       mobilephone=mobilephone,
                       email=email,
                       email2=email2,
                       email3=email3
                       )

