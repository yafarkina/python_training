#  -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test_new", header ="test_new", footer ="test_new"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)



#def test_delete_group(app, db):
#    if app.group.count() == 0:
 #       app.group.create(Group(name="test_new", header ="test_new", footer ="test_new"))
    #old_groups = app.group.get_group_list()
   # index = randrange(len(old_groups))
   # app.group.delete_group_by_index(index)
   # assert len(old_groups) - 1 == app.group.count()
    #new_groups = app.group.get_group_list()
   #old_groups[index:index+1] = []
   # assert old_groups == new_groups