# in the_bank.py
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank:
# an even number of attributes -> nbr % 2 == 0
# an attribute starting with b -> 
# no attribute starting with zip or addr
# no attribute name, id and value
    pass
