from datetime import datetime

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {
			'starter': [],
			'lunch': [],
			'desert': []
		}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for recipe in self.recipes_list.keys():
			for tp in self.recipes_list.get(recipe):
				if tp.name == name:
					for att in tp.__dict__.keys():
						print(f"{att}: {tp.__dict__[att]}")

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for recipe in self.recipes_list.keys():
			if recipe_type == recipe:
				for r in self.recipes_list[recipe_type]:
					print(r.name)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.last_update = datetime.now()
		for r in self.recipes_list.keys():
			if recipe.recipe_type == r:
				self.recipes_list.get(r).append(recipe)
