import json
with open('recipes.txt', 'r', encoding='utf-8') as file:
  cook_book = {}
  for line in file:
    dish_name = line.strip()
    ingredients_count = int(file.readline().strip())
    ingredients = []
    for i in range(ingredients_count):
      ingredient = file.readline().strip()
      ingredient_name, quantity, measure = ingredient.split('|')
      ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
      ingredients.append(ingredient_dict)
    cook_book[dish_name] = ingredients
    file.readline()

# json_data = json.dumps(cook_book, indent=4, sort_keys=False, ensure_ascii=False)
# print(json_data)
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient['ingredient_name']
        quantity = int(ingredient['quantity']) * person_count
        measure = ingredient['measure']
        if ingredient_name in shop_list:
          shop_list[ingredient_name]['quantity'] += quantity
        else:
          shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
  return shop_list


shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
print(shop_list)




