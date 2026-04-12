import re
import random
from model.contact import Contact


def test_personal_data_on_home_page(app, db, check_ui):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_bd = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_bd, key=Contact.id_or_max)



#def test_personal_data_on_home_page_old(app, check_ui):  #старый вариант кейса
#    contact_from_home_page = app.contact.get_contact_list()[0]
 #   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
 #   assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
#    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
#    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_on_view_page_db(app, db, check_ui):
    contacts_from_bd = db.get_contact_list()
    contact = random.choice(contacts_from_bd)
    contact_from_view_page = app.contact.get_contact_info_from_view_page_by_id(contact.id)
    assert contact_from_view_page == contact


#def test_contact_on_view_page(app, db, check_ui):
 #   contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
 #   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
 #   assert contact_from_view_page.firstname == clear(contact_from_edit_page.firstname)
#    assert contact_from_view_page.lastname == clear(contact_from_edit_page.lastname)
 #   assert clear(contact_from_view_page.address) == clear(contact_from_edit_page.address)
 #   assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
 #   assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
 #   assert contact_from_view_page.email == contact_from_edit_page.email
 #   assert contact_from_view_page.email2 == contact_from_edit_page.email2
 #   assert contact_from_view_page.email3 == contact_from_edit_page.email3

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter (lambda x: x is not None,
                                 [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter (lambda x: x is not None,
                                         [contact.email, contact.email2, contact.email3]))))