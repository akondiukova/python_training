import pytest
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New_name")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(name="Name"))
    app.group.test_mofify_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Name",header="header"))
    app.group.test_mofify_first_group(Group(header="New_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
