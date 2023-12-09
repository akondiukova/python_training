import pytest
from model.contact import Contact
from fixture.application import Application
from random import randrange



def test_edit_name_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Petrov")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
    app.contact.test_edit_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_birth_day_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(birth_day="3")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov", "Ivan", "Ivanov", "ivan", "title", "Company",
                                        "Nizhny Novgorod, Bolshaya Pokrovskaya, 100",
                                        "65-66-55", "8906746322", "75-65-32", "test1@test.ru", "test1@test.ru",
                                        "test3@test.ru",
                                        "www://homepage", "14", "June", "2000", "5", "June", "2010",
                                        "Nizhny Novgorod", "76", "120"))
    app.contact.test_edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)