from sys import maxsize

class Contact:
   def __init__(self,
                firstname =None, lastname = None,
                company = None, address = None,
                homephone = None, workphone= None, mobilephone= None,
                email = None, email2 = None, email3 = None,
                id = None):
       self.firstname = firstname
       self.lastname = lastname
       self.company = company
       self.address = address
       self.homephone = homephone
       self.workphone = workphone
       self.mobilephone = mobilephone
       self.email = email
       self.email2 = email2
       self.email3 = email3
       self.id = id

   def __repr__(self):
       return "%s:%s" % (self.id, self.firstname)

   def __eq__(self, other):
       return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

   def id_or_max(self):
       if self.id:
           return int(self.id)
       else:
            return maxsize