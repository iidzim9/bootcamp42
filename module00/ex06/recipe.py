import string

cookbook = {
    'sandwich' : { 
        'ingredients': ['ham', 'bread' , 'cheese' ,'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'
    },
    'cake' : {
        'ingredients': ['flour', 'sugar' , 'eggs'],
        'meal': 'desert',
        'prep_time': '60'
    },
    'salade' : {
        'ingredients': ['avocado' , 'arugula' , 'tomatoes' , 'spinach'],
        'meal': 'lunch',
        'prep_time' : '15'
    }
}


    
def add_recipe():
    print("add a recipe")
    name = input("recipe:\t")
    ingredients = input("ingredients:\t").split()
    meal = input("meals:\t")
    prep_time = input("prep_time\t")
    cookbook[name]={'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}

def delete_recipe():
    key = input("delete a recipe \n")
    del cookbook[key]

def print_recipe():
    key = input("Please enter the recipe's name to get its details:\n>> ")
    s = cookbook.get(key)
    if not s:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
        return
    print("Recipe for " + key)
    print(f"Ingredients list: {s['ingredients']}")
    print(f"To be eaten for {s['meal']}")
    print(f"Takes {s['prep_time']} minutes of cooking")


def print_cookbook():
    print(cookbook)


def quit_cookbook():
    print("Cookbook closed.")
    exit()

def funct():
    while True:
        x = int(input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> "))
        if x == 1:
            add_recipe()
        elif x == 2:
            delete_recipe()
        elif x == 3:
            print_recipe()
        elif x == 4:
            print_cookbook()
        elif x == 5:
            quit_cookbook()
        else:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")

funct()