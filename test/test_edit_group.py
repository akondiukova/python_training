import pytest
from model.group import Group

def test_modify_group_name(app):
    app.session.auth("admin", "secret")
    app.group.test_mofify_first_group(Group(name="New_name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.auth("admin", "secret")
    app.group.test_mofify_first_group(Group(header="New_header"))
    app.session.logout()