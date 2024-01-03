import pytest
from model.group import Group
from random import randrange
import random

def test_modify_group_name(app,orm,check_ui):
    # old_groups = app.group.get_group_list()
    old_groups = orm.get_group_list()
    group_new = Group(name="name56")
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    # group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(name="Name"))
    app.group.test_mofify_group_by_id(group_new,group.id)
    # new_groups = app.group.get_group_list()
    new_groups = orm.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    old_groups.append(group_new)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Name",header="header"))
    app.group.test_mofify_first_group(Group(header="New_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
