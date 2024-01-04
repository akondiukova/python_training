import random


def test_delete_contact_from_group(app,orm,check_ui):
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    if len(orm.get_contacts_in_group(group)) == 0:
        old_contacts = orm.get_contact_list()
        contact_for_add_group = random.choice(old_contacts)
        app.contact.add_contact_in_group_by_id(contact_for_add_group.id, group.id)
    contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group_by_id(contact.id,group.id)
    contact_in_group = orm.get_contacts_in_group(group)
    assert contact not in contact_in_group