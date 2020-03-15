#!/usr/bin/env python3
import os
import urllib.parse

recipe_directory = "rezepte"

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
        categories[category.name][recipe_name] = urllib.parse.quote(recipe.name)

        all_recipes[recipe_name] = os.path.join(category.name, urllib.parse.quote(recipe.name))

with open(os.path.join(recipe_directory, 'index.md'), 'w+') as index_file:
    for category in sorted(categories):
        index_file.write(f'[{category}]({category}/index.md)\n\n')

        with open(os.path.join(recipe_directory, category, 'index.md'), 'w+') as category_file:
            for recipe in sorted(categories[category]):
                category_file.write(f'[{recipe}]({categories[category][recipe]})\n\n')

with open(os.path.join(recipe_directory, 'all.md'), 'w+') as file:
    for recipe in sorted(all_recipes):
        file.write(f'[{recipe}]({all_recipes[recipe]})\n\n')
