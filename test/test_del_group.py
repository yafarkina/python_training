#  -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.delete_first_group()
    app.group.return_to_group_page()
    app.session.logout()
