import pytest
from model.contact import Contact
import random
import string
from datetime import datetime

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits_and_punctuation(maxlen):
    symbols = string.digits + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen,maxlen_cod):
    symbols = string.ascii_letters + string.punctuation
    only_ascii_letters = string.ascii_letters
    us_name = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    domain_name = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    cod = "".join([random.choice(only_ascii_letters) for i in range(random.randrange(maxlen_cod))])
    return us_name + "@" + domain_name + "." + cod

def random_day():
    day = random.randint(1, 31)
    print("day = " + "%s"%day)
    return "%s"%day


def random_month():
    months = ["-","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)

def random_year():
    return "%s"%random.randint(1900, datetime.now().year)


testdata = [
    Contact(first_name = random_string("first_name",10), middle_name = random_string("middle_name",20),
            last_name = random_string("last_name", 20), nickname = random_string("nickname", 10),
            title = random_string("title", 10), company = random_string("company", 10),
            home_phone = random_digits_and_punctuation(20), mobile_phone = random_digits_and_punctuation(20), work_phone = random_digits_and_punctuation(20),
            email = random_email(10,6), birth_day = random_day(), birth_month = random_month(), birth_year = random_year())
    for i in range(3)
]

@pytest.mark.parametrize("contact",testdata,ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    #contact = Contact("Ivanov","Ivan","Ivanov","ivan", "title","Company","Nizhny Novgorod, Bolshaya Pokrovskaya, 100",
    #                                     "65-66-55","8906746322","75-65-32","test1@test.ru","test1@test.ru","test3@test.ru",
    #                                    "www://homepage","14","June","2000","5","June","2010",
    #                                     "Nizhny Novgorod","76","120")
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


