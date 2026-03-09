#  -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password= "secret")
    app.open_contact_page()
    app.create_contact(Contact(firstname = "first", lastname = "last", company = "company", address = "address", telephone = "home"))
    app.return_to_home_page()
    app.logout()






