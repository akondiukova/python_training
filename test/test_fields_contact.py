import re
from random import randrange

def test_fields_contact(app,orm):
    old_contacts = orm.get_contact_list()
    for contact in old_contacts:
        assert contact.last_name == app.contact.get_contact_info_by_id(contact.id).last_name
        assert contact.first_name == app.contact.get_contact_info_by_id(contact.id).first_name
        assert contact.address == app.contact.get_contact_info_by_id(contact.id).address
        assert merge_phones_like_on_home_page(contact) == app.contact.get_contact_info_by_id(contact.id).all_phones_from_home_page
        assert merge_emails_on_home_page(contact) == app.contact.get_contact_info_by_id(
            contact.id).all_emails

   # contact_from_home_page = app.contact.get_contact_list()[index]
   # contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_id(id)
    #  assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    #  assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    #  assert contact_from_home_page.address == contact_from_edit_page.address
    #  assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.all_emails == merge_emails_on_home_page(contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.sec_home]))))

def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None,[contact.email, contact.email2, contact.email3]))

def clear(s):
    return re.sub("[() -]","", s)