class Contact:
   def __init__(self, firstname =None, lastname = None, company = None, address = None, telephone = None, id = None):
       self.firstname = firstname
       self.lastname = lastname
       self.company = company
       self.address = address
       self.telephone = telephone
       self.id = id

   def __repr__(self):
       return "%s:%s" % (self.id, self.firstname)

   def __eq__(self, other):
       return self.id == other.id and self.firstname == other.firstname