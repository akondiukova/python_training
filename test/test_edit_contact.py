import pytest
from model.contact import Contact
from fixture.application import Application


def test_edit_first_name_contact(app):
    app.contact.test_edit_contact(Contact(first_name="Petrov"))


def test_edit_birth_day_contact(app):
    app.contact.test_edit_contact(Contact(birth_day="3"))