#  -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname ="first_new", lastname ="last_new", company ="company_new", address ="address_new", telephone ="home_new"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname ="first_edit", lastname ="last_edit", company ="company_edit", address ="address_edit", telephone ="home_edit")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



