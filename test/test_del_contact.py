#  -*- coding: utf-8 -*-
import random
from model.contact import Contact

def test_delete_contact(app, db, check_ui):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname ="first_new", lastname ="last_new", company ="company_new", address ="address_new", mobilephone ="79198765432"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
 #   assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)


#def test_delete_contact(app, db):
 #   if app.contact.count() == 0:
#       app.contact.create(Contact(firstname ="first_new", lastname ="last_new", company ="company_new", address ="address_new", mobilephone ="79198765432"))
   # old_contacts = app.contact.get_contact_list()
 #   index = randrange(len(old_contacts))
  #  app.contact.delete_contact_by_index(index)
 #   assert len(old_contacts) - 1 == app.contact.count()
  #  new_contacts = app.contact.get_contact_list()
 #   old_contacts[index:index+1] = []
#    assert old_contacts == new_contacts