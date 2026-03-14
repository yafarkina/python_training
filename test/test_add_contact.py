#  -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
  #  app.session.login(username="admin", password= "secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname ="first", lastname ="last", company ="company", address ="address", telephone ="home"))
    app.contact.return_to_home_page()
  #  app.session.logout()






