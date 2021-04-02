class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return 'name: {self.name}\ncooking_lvl: {self.cooking_lvl}\ncooking_time: {self.cooking_time}\n\
            ingredients: {self.ingredients}\ndescription: {self.description}\nrecipe_type: {self.recipe_type}\n'.format(self=self)

