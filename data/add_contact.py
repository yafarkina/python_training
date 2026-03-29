import random
import string
from model.contact import Contact

constant = [
Contact(firstname= "first_name_person_one",
        lastname= "last_name_person_one",
        company= "company1",
        address= "address1",
        homephone= "12345678",
        mobilephone= "79001234567",
        workphone= "12345678",
        email= "test1@test1.test",
        email2= "test2@test1.test",
        email3= "test3@test1.test"
            ),
Contact(firstname= "first_name_person_two",
        lastname= "last_name_person_two",
        company= "company2",
        address= "address2",
        homephone= "12345678",
        mobilephone= "12345678",
        workphone= "12345678",
        email= "test1@test2.test",
        email2= "test2@test2.test",
        email3= "test3@test2.test"
            )
]

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
    for i in range(0)
]
