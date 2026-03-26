#  -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname ="first_name", lastname ="last_name",
                      company ="company", address ="address",
                      homephone ="123456", mobilephone="70123456789", workphone="123678",
                      email="test@test.test", email2="test@test.test", email3="test@test.test"
                      )
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)







