import pytest
from model.contact import Contact
from fixture.application import Application

def test_add_contact(app):
    old_groups = app.contact.get_contact_list()
    contact = Contact("Ivanov","Ivan","Ivanov","ivan", "title","Company","Nizhny Novgorod, Bolshaya Pokrovskaya, 100",
                                         "65-66-55","8906746322","75-65-32","test1@test.ru","test1@test.ru","test3@test.ru",
                                         "www://homepage","14","June","2000","5","June","2010",
                                         "Nizhny Novgorod","76","120")
    app.contact.add_contact(contact)
    new_groups = app.contact.get_contact_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(contact)
    assert sorted(old_groups, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)


