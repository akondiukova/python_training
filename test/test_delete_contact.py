import pytest
from fixture.application import Application
from model.contact import Contact
from random import randrange
import random

def test_delete_contact(app,orm,check_ui):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
    # old_contacts = app.contact.get_contact_list()
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    #  index = randrange(len(old_contacts))
    app.contact.test_delete_contact_by_id(contact.id)
    # new_contacts = app.contact.get_contact_list()
    new_contacts = orm.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    # old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

