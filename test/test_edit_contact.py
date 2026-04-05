#  -*- coding: utf-8 -*-
import random
from model.contact import Contact

def test_edit_contact(app, db, json_contacts, check_ui):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname ="first_name", lastname ="last_name",
                      company ="company", address ="address",
                      homephone ="123456", mobilephone="70123456789", workphone="123678",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test"))
    contact_new_data = json_contacts
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact_new_data, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_new_data)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)



