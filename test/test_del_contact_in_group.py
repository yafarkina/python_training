import random
from model.contact import Contact
from model.group import Group


def test_del_contact_in_group(app, orm, check_ui):
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test_new", header="test_new", footer="test_new"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.create(Contact(firstname="first_new", lastname="last_new", company="company_new", address="address_new", mobilephone="79198765432"))
        contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts)
        app.contact.add_contact_in_group(contact.id, group.id)
    contacts = orm.get_contacts_in_group(group)
    old_contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.del_contact_in_group(contact.id, group.id)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


