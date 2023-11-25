import pytest
from model.contact import Contact
from fixture.application import Application


def test_edit_contact(app):
    app.session.auth("admin", "secret")
    app.contact.test_edit_contact(Contact("Petrov","Petr","Petrovich","petya", "title","Company","Nizhny Novgorod, Bolshaya Pokrovskaya, 100",
                                         "65-66-55","8906746322","75-65-32","test1@test.ru","test1@test.ru","test3@test.ru",
                                         "www://homepage_new","30","June","2000","8","June","2010",
                                         "Nizhny Novgorod","33423","34234"))
    app.session.logout()