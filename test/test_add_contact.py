#  -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password= "secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname ="first", lastname ="last", company ="company", address ="address", telephone ="home"))
    app.contact.return_to_home_page()
    app.session.logout()






