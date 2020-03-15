#!/usr/bin/env python3
import os

recipe_directory = u'rezepte'

categories = {}
all_recipes = {}

for category in os.scandir(recipe_directory):
    if not category.is_dir():
        continue

    for recipe in os.scandir(category.path):
        if not recipe.is_file() or not recipe.path.endswith(".md") or recipe.name == 'index.md':
            continue

        recipe_name = os.path.splitext(recipe.name)[0]

        categories.setdefault(category.name, {})
        categories[category.name][recipe_name] = recipe.name

        all_recipes[recipe_name] = os.path.join(category.name, recipe.name)

#print(categories)
#print(all_recipes)

with open(os.path.join(recipe_directory, 'index.md'), 'w+') as index_file:
    index_file.write('# Kategorien\n\n')

    for category in sorted(categories):
        category_name = category.replace('_', ' ')
        index_file.write(f'[{category_name}]({category}/index.md)\n\n')

        with open(os.path.join(recipe_directory, category, 'index.md'), 'w+') as category_file:
            category_file.write(f'# {category_name}\n\n')

            for recipe in sorted(categories[category]):
                recipe_name = recipe.replace('_', ' ')
                category_file.write(f'[{recipe_name}]({categories[category][recipe]})\n\n')

with open(os.path.join(recipe_directory, 'all.md'), 'w+') as file:
    file.write('# Alle Rezepte\n\n')

    for recipe in sorted(all_recipes):
        recipe_name = recipe.replace('_', ' ')
        file.write(f'[{recipe_name}]({all_recipes[recipe]})\n\n')
