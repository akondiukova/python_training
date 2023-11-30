import pytest
from model.contact import Contact
from fixture.application import Application


def test_edit_first_name_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
    app.contact.test_edit_contact(Contact(first_name="Petrov"))


def test_edit_birth_day_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact("Ivanov", "Ivan", "Ivanov", "ivan", "title", "Company",
                                        "Nizhny Novgorod, Bolshaya Pokrovskaya, 100",
                                        "65-66-55", "8906746322", "75-65-32", "test1@test.ru", "test1@test.ru",
                                        "test3@test.ru",
                                        "www://homepage", "14", "June", "2000", "5", "June", "2010",
                                        "Nizhny Novgorod", "76", "120"))
    app.contact.test_edit_contact(Contact(birth_day="3"))