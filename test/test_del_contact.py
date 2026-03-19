#  -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
       app.contact.open_contact_page()
       app.contact.create(Contact(firstname ="first_new", lastname ="last_new", company ="company_new", address ="address_new", telephone ="home_new"))
       app.contact.return_to_home_page()
    app.contact.delete_first_contact()
