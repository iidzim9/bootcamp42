class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True

# Class Stark inherits GotCharacter   
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive=False

child = Stark("child1")
print(child.__dict__)
child.print_house_words()
print(child.is_alive)
child.die()
print(child.is_alive)
