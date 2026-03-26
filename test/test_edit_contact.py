#  -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname ="first_name", lastname ="last_name",
                      company ="company", address ="address",
                      homephone ="123456", mobilephone="70123456789", workphone="123678",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname ="first_name", lastname ="last_name",
                      company ="company", address ="address",
                      homephone ="123456", mobilephone="70123456789", workphone="123678",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact,index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



