#  -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.ctreate(Group(name ="test", header ="test", footer ="test"))
    app.group.return_to_group_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.ctreate(Group(name ="", header ="", footer =""))
    app.group.return_to_group_page()
    app.session.logout()

