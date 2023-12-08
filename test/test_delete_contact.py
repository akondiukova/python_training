import pytest
from fixture.application import Application
from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
    old_contacts = app.contact.get_contact_list()
    app.contact.test_delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts