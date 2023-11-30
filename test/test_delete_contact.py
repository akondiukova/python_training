import pytest
from fixture.application import Application
from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
    app.contact.test_delete_contact()