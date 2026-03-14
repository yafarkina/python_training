#  -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name ="test_edit", header ="test_edit", footer ="test_edit"))
