import sys
import cumenu
import time
import re
import math
import json

meals = ["Breakfast", "Lunch", "Dinner"]
date = time.strftime("%Y-%m-") + str(int(time.strftime("%d")) + 0)

def loadMenus():
    with open('data/tastedata.json', 'r') as fp:
        foods = json.load(fp)
    for x in range(-8,7): # determine range of time to load data from, hardcoded for now
        date = time.strftime("%Y-%m-") + str(int(time.strftime("%d")) + x)
        for eatery in cumenu.getOptions(meals[2], date, False):
            currmenu = cumenu.getMenu(eatery, meals[2], date)
            for item in currmenu:
                if not(item in foods):
                    foods[item] = -1;
        print(date + " done")
    with open("data/tastedata.json", "w") as file:
        json.dump(foods, file)
    print("Loaded.")


def indexTasteData():
    with open('data/indexed_taste_data.json', 'r') as fp:
        index = json.load(fp)
    with open('data/tastedata.json', 'r') as fp:
        foods = json.load(fp)
    for food in foods:
        for word in food.split():
            w = word.lower()
            if not(w in index):
                index[w] = {"score": -1, "items": [food]}
            else:
                if not(w in index[w]["items"]):
                    index[w]["items"] += [food]
    with open("data/indexed_taste_data.json", "w") as file:
        json.dump(index, file)
    print("Indexed!")

def train():
    foods = {}
    with open('data/tastedata.json', 'r') as fp:
        foods = json.load(fp)
    for food in foods:
        if(foods[food] == -1):
            inp = raw_input(food + "\n")
            if(inp == "0" or inp == "1" or inp == "2" or inp == "3" or inp == "4" or inp == "5"):
                foods[food] = float(inp)/5
            if(inp == "q"):
                with open("data/tastedata.json", "w") as file:
                    json.dump(foods, file)
                print("Exiting.")
                exit()
    with open("data/tastedata.json", "w") as file:
        json.dump(foods, file)
    print("fully trained!")
    print("indexing...")
    indexTasteData()

def scoreIndex():
    with open('data/tastedata.json', 'r') as fp:
        taste = json.load(fp)
    with open('data/indexed_taste_data.json', 'r') as fp:
        index = json.load(fp)
    for item in index:
        total = 0
        totscore = 0
        for food in index[item]["items"]:
            total += 1
            totscore += taste[food]
            # print(food + ":" + str(taste[food]) + ", " + str(totscore))
        index[item]["score"] = totscore/total 
    with open("data/indexed_taste_data.json", "w") as file:
        json.dump(index, file)
    print("Scored the index.")

if(sys.argv[1] == "load"):
    loadMenus()
elif(sys.argv[1] == "train"):
    train()
elif(sys.argv[1] == "index"):
    indexTasteData()
    scoreIndex()