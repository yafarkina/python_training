#  -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact

def random_string_fio(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_email(maxlen):
    domain_list =["@gmail.com", "@ya.ru", "@mail.ru"]
    symbols = string.ascii_letters + string.digits + "." + "-" + "_" + "+"
    local_part = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return local_part + random.choice(domain_list)

testdata = [
    Contact(firstname= random_string_fio("first_name",10),
            lastname= random_string_fio("last_name",10),
            company= random_string_str("company", 20),
            address= random_string_str("address", 30),
            homephone= random_string_phone(8),
            mobilephone= random_string_phone(11),
            workphone= random_string_phone(8),
            email= random_string_email(10),
            email2= random_string_email(10),
            email3= random_string_email(10)
            )
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

