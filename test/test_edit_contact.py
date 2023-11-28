import pytest
from model.contact import Contact
from fixture.application import Application


def test_edit_first_name_contact(app):
    app.session.auth("admin", "secret")
    app.contact.test_edit_contact(Contact(first_name="Petrov"))
    app.session.logout()

def test_edit_birth_day_contact(app):
    app.session.auth("admin", "secret")
    app.contact.test_edit_contact(Contact(birth_day="3"))
    app.session.logout()