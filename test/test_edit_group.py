import pytest
from model.group import Group

def test_delete_group(app):
    app.session.auth("admin", "secret")
    app.group.test_edit_group(Group("new_name", "new_header", "new_footer"))
    app.session.logout()