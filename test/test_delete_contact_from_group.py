import random
from model.group import Group
from model.contact import Contact


def test_delete_contact_from_group(app,orm,check_ui):
    old_groups = orm.get_group_list()
    old_contacts = orm.get_contact_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="test"))
        old_groups = orm.get_group_list()
    if len(old_contacts) == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
        old_contacts = orm.get_contact_list()
    group = random.choice(old_groups)
    if len(orm.get_contacts_in_group(group)) == 0:
        contact_for_add_group = random.choice(old_contacts)
        app.contact.add_contact_in_group_by_id(contact_for_add_group.id, group.id)
    contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group_by_id(contact.id,group.id)
    contact_in_group = orm.get_contacts_in_group(group)
    assert contact not in contact_in_group