from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
           wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        # select first_group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        # select group by index
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_fild_value("group_name", group.name)
        self.change_fild_value("group_header", group.header)
        self.change_fild_value("group_footer", group.footer)

    def change_fild_value(self, fild_name, fild_value):
        wd = self.app.wd
        if fild_value is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(fild_value)

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_first_group(self):
        wd = self.app.wd
        self.edit_group_by_index(0)

    def edit_group_by_index(self,group,index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open page edit
        wd.find_elements_by_name("edit")[index].click()
        # fill form
        self.fill_group_form(group)
        #submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None


    def modify_first_group(self):
        wd = self.app.wd
        self.modify_group_by_index(0)

    def modify_group_by_index(self, new_group_data, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open page edit
        wd.find_elements_by_name("edit")[index].click()
        # fill form
        self.fill_group_form(new_group_data)
        # submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

