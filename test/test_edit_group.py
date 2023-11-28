import pytest
from model.group import Group

def test_modify_group_name(app):
    app.group.test_mofify_first_group(Group(name="New_name"))

def test_modify_group_header(app):
    app.group.test_mofify_first_group(Group(header="New_header"))