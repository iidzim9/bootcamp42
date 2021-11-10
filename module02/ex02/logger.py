import time
from datetime import date, datetime
from random import randint

def log(function):
	def wrapper(*argc, **kwargs):
		start_time = datetime.now()
		fd = open("machine.log", "a")
		fd.write("(cmaxime)Running: -> ");
		fd.write(function.__name__);
		fd.write(f"		[ exec-time = {(datetime.now() - start_time)} ms ]\n")
		fd.close()
	return wrapper

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
	  if self.water_level > 20:
		  return True
	  else:
		  print("Please add water!")
		  return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	# current_time = datetime.now()
	# print(">>> ", (current_time - datetime.now()) / 3600)
	# print(datetime.now())
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)
