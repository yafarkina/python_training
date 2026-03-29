import random
import string
import os.path
import json
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
