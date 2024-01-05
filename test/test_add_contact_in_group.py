from model.group import Group
from model.contact import Contact
import random

def test_add_contact_in_group(app,orm,check_ui):
    old_contacts = orm.get_contact_list()
    old_groups = orm.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="test"))
        old_groups = orm.get_group_list()
    if len(old_contacts) == 0:
        app.contact.add_contact(Contact("Ivanov","Ivan","Ivanov","ivan"))
        old_contacts = orm.get_contact_list()
    n=0
    for group in old_groups:
        contacts_out_of_group = orm.get_contacts_not_in_group(group)
        if len(contacts_out_of_group) != 0:
            contact = random.choice(contacts_out_of_group)
            app.contact.add_contact_in_group_by_id(contact.id, group.id)
            contacts_in_group = orm.get_contacts_in_group((Group(id=group.id)))
            assert contact in contacts_in_group
            break
        else:
            n+=1
            continue
    if n == len(old_groups):
        print("Все контакты добавлены в группы!")
        app.group.create(Group(name="test"))
        new_group = orm.get_group_list()[-1]
        contact = random.choice(old_contacts)
        app.contact.add_contact_in_group_by_id(contact.id, new_group.id)
        contacts_in_new_group = orm.get_contacts_in_group(new_group)
        assert contact in contacts_in_new_group





    # contacts_out_of_group = orm.get_contacts_not_in_group()
    # if len(contacts_out_of_group)!= 0:
    #     contact = random.choice(contacts_out_of_group)
    #     app.contact.add_contact_in_group_by_id(contact.id, group.id)
    #     contacts_in_group = orm.get_contacts_in_group((Group(id=group.id)))
    #     assert contact in contacts_in_group


