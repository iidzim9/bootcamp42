from book import Book
from recipe import Recipe

tourte = Recipe('cake', 3, 60, ['sugar','eggs','sugar'], 'description', 'desert')
to = Recipe('ca', 34, 6450, ['sugar','eggs','sugar'], '', 'desert')
# print(str(tourte))

cookbook = Book('CookBook')
print(cookbook.__dict__)
cookbook.add_recipe(tourte)
cookbook.add_recipe(to)
cookbook.get_recipe_by_name('cake')
cookbook.get_recipes_by_types('desert')