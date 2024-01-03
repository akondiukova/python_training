import pytest
from model.group import Group
import random

def test_delete_group(app,db,orm,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # old_groups = db.get_group_list()
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.test_delete_group_by_id(group.id)
    # new_groups = db.get_group_list()
    new_groups = orm.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)
