#  -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.edit_first_contact(Contact(firstname ="first_edit", lastname ="last_edit", company ="company_edit", address ="address_adit", telephone ="home_edit"))



