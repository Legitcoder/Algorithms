#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_quantity = list(recipe.values())
  ingredients_quantity = list(ingredients.values())
  if len(recipe_quantity) > len(ingredients_quantity): return 0
  amount = 1
  for i in range(len(recipe_quantity)):
    recipe_value = recipe_quantity[i]
    if ingredients_quantity[i] > recipe_quantity[i]:
      ingredients_quantity[i] -= recipe_value
      if ingredients_quantity[i] < 0: break
      if i == len(recipe_quantity) - 1: amount += 1

  return amount - 1




print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {'milk': 1288, 'flour': 9, 'sugar': 95}))
print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {'milk': 198, 'butter': 52, 'cheese': 10}))
print(recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {'milk': 5, 'sugar': 120, 'butter': 500}))
print(recipe_batches({'milk': 2}, {'milk': 200}))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))