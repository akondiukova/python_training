import pytest
from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name"))
    app.group.test_mofify_first_group(Group(name="New_name"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name",header="header"))
    app.group.test_mofify_first_group(Group(header="New_header"))