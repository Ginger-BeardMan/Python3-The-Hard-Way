import random

# 5 real world lists:

favorite_foods = ['Pizza', 'Beer', 'Pineapple', 'Strawberries', 'Carrots']

favorite_movies = ['Pulp Fiction', 'Blade Runner', 'LOTR', 'Your Highness']

home_depot_list = ['Insulation', 'Garden Pots', '1x4s', 'Kid Project']

pancake_ingredients = ['Flour', 'Egg', 'Baking Powder', 'Cinnamon', 'Milk']

specialty_ingredients = ['Chocolate Chips', 'Bananas', 'Blueberries', 'Strawberries']

while len(pancake_ingredients) != 7:
	recipe = specialty_ingredients.pop(random.randrange(len(specialty_ingredients)))
	pancake_ingredients.append(recipe)
	print(f"Your new recipe is: ", " ".join(pancake_ingredients))

tea = ['Earl Gray', 'Rooibos', 'Camomile']

# Scripts for lists:

# .pop()

# .append()

# .join()