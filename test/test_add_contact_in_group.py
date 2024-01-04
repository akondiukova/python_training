from model.group import Group
import random


def test_add_contact_in_group(app,orm,check_ui):
    old_contacts = orm.get_contact_list()
    old_groups = orm.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    app.contact.add_contact_in_group_by_id(contact.id,group.id)
    contacts_in_group = orm.get_contacts_in_group((Group(id=group.id)))
    assert contact in contacts_in_group


