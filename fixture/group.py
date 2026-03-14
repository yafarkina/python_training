class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()

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

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_fild_value("group_name", group.name)
        self.change_fild_value("group_header", group.header)
        self.change_fild_value("group_footer", group.footer)
        #wd.find_element_by_name("group_name").click()
        #wd.find_element_by_name("group_name").clear()
       # wd.find_element_by_name("group_name").send_keys(group.name)
        #wd.find_element_by_name("group_header").click()
        #wd.find_element_by_name("group_header").clear()
       # wd.find_element_by_name("group_header").send_keys(group.header)
       # wd.find_element_by_name("group_footer").click()
       # wd.find_element_by_name("group_footer").clear()
      #  wd.find_element_by_name("group_footer").send_keys(group.footer)

    def change_fild_value(self, fild_name, fild_value):
        wd = self.app.wd
        if fild_value is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(fild_value)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first_group(self,group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # open page edit
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(group)
        #submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self, wd):
        # select first_group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # open page edit
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(new_group_data)
        # submit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()