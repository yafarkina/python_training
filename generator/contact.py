import random
import string
from model.contact import Contact

def random_string_fio(prefix, max_len):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

def random_string_str(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

def random_string_phone(max_len):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

def random_string_email(max_len):
    domain_list =["@gmail.com", "@ya.ru", "@mail.ru"]
    symbols = string.ascii_letters + string.digits + "." + "-" + "_" + "+"
    local_part = "".join([random.choice(symbols) for i in range(random.randrange(max_len))])
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
    for i in range(1)
]
