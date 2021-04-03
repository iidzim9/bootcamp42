from book import Book
from recipe import Recipe

tourte = Recipe('cake', 3, 60, ['sugar','eggs','sugar'], 'description', 'desert')
to = Recipe('crepe', 4, 45, ['sugar','eggs','sugar'], '', 'desert')
print(str(tourte))

cookbook = Book('CookBook')
# print(cookbook.__dict__)
if not tourte.check_pass_fail():
    print("invalid recipe")
    exit()
if not to.check_pass_fail():
    print("invalid recipe")
    exit()
cookbook.add_recipe(tourte)
cookbook.add_recipe(to)
cookbook.get_recipe_by_name('cake')
cookbook.get_recipes_by_types('desert')
