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

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self,group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open page edit
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(group)
        #submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open page edit
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))
