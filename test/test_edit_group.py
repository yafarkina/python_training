#  -*- coding: utf-8 -*-
import random
from model.group import Group


def test_edit_group(app, db, json_groups, check_ui):
    if app.group.count() == 0:
       app.group.create(Group(name="test_new", header ="test_new", footer ="test_new"))
    group_new_data = json_groups
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group_new_data, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    group_new_data.id = group.id
    old_groups.append(group_new_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_new", header="test_new", footer="test_new"))
#    old_groups = app.group.get_group_list()
 #   index = randrange(len(old_groups))
#    group = Group(name ="new name")
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(group, index)
 #   new_groups = app.group.get_group_list()
 #   assert len(old_groups) == len(new_groups)
 #   old_groups[index]=group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)