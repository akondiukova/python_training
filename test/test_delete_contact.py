import pytest
from fixture.application import Application

def test_edit_contact(app):
    app.session.auth("admin", "secret")
    app.contact.test_delete_contact()
    app.session.logout()