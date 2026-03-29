import random
import string
from model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data =[
    Group(name = name, header = header, footer = footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

testdata_empty = [Group(name = "", header = "", footer = "")]

testdata_generated = [Group(name = random_string("name", 10),
           header = random_string("header", 20),
           footer = random_string("footer", 20))
           for i in range(0)
        ]

testdata = testdata_empty + testdata_generated
