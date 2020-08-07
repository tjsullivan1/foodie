import microdata
import os
import requests


def main():
    file = os.path.join('c:/Users/tjsul/OneDrive/Documents/Hobbies/Cooking/Recipes', 'Alexander.html')

    with open(file, 'r') as recipe:
        print(convert_recipe(recipe))



def convert_recipe(recipe):
    items = microdata.get_items(recipe)
    item = items[0]
    item.itemtype
    item.name

    return item.json()


if __name__ == '__main__':
    main()
