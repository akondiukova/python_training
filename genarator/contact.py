import random
import string
from model.contact import Contact
from datetime import datetime
import os.path
import jsonpickle
import getopt
import sys

try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
out = "../data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), out)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))