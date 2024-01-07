from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table = "address_in_groups", column="id", reverse="groups")


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        email= Optional(str, column='email')
        email2= Optional(str, column='email2')
        email3= Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table = "address_in_groups", column="group_id", reverse="contacts")

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host = host, database = name, user = user,
                                         password = password)
        self.db.generate_mapping()

    def convert_groups_to_model(self,groups):
        def convert(group):
            return  Group(id=str(group.id), name = group.name, header = group.header, footer = group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self,contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name = contact.firstname, last_name = contact.lastname,
                           address = contact.address, home_phone = contact.home_phone, mobile_phone = contact.mobile_phone, work_phone = contact.work_phone,
                           email = contact.email, email2 = contact.email2, email3 = contact.email3)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))


    @db_session
    def get_contacts_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return (self.convert_contacts_to_model
                (select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))

    @db_session
    def is_contact_in_group(self, contact):
        orm_list_group = self.get_group_list()

    def all_contacts_are_in_all_groups(self):
        group_list = self.get_group_list()
        contact_list = self.get_contact_list()
        res = True
        for group in group_list:
            contact_in_groups = self.get_contacts_in_group(group)
            res = res and (all(contact in contact_in_groups for contact in contact_list))
        return res




