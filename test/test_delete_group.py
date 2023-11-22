import pytest

def test_delete_group(app):
    app.session.auth("admin", "secret")
    app.group.test_delete_first_group()
    app.session.logout()