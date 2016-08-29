import sys
import cumenu
import time
import json
import operator
import math

eaterycodes = {1: "Cook House Dining Room", 2: "Becker House Dining Room", 3: "Keeton House Dining Room", 4: "Rose House Dining Room", 5: "Hans Bethe House - Jansens Dining Room", 6: "Robert Purcell Marketplace Eatery", 7: "North Star", 8: "Risley Dining", 9: "104 West!", 10: "Okenshields"}
meals = ["Breakfast", "Lunch", "Dinner"]
date = time.strftime("%Y-%m-") + str(int(time.strftime("%d")) + 6)

def getBestDining():
    score = {}
    taste = {}
    with open('data/tastedata.json', 'r') as fp:
        taste = json.load(fp)
    # for eatery in cumenu.getOptions(meals[2], date, False):
    for eatery in cumenu.getOptions(meals[2], date, False):
        score[eatery] = getModDiningScore(taste, int(eatery))

    best = int(max(score, key=score.get))
    print("Go to " + eaterycodes[best])
    # dic = getDiningDic(taste, best)
    # maxval = dic[max(dic, key=dic.get)]
    # print(maxval)
    # # scdic = getDiningDic(taste, best)
    # for key, value in dic.items():
    #     if(float(value) == maxval):
    #         print(key)

def getDiningScore(tastedic, eatery):
    score = 0;
    total = 0;
    for food in cumenu.getMenu(eatery, meals[2], date):
        if food in tastedic.keys():
            score += tastedic[food]
            total += 1
    print(eatery + ": " + str(score));
    return score

def getDiningDic(tastedic, eatery):
    dic = {0: 0}
    for food in cumenu.getMenu(eatery, meals[2], date):
        if food in tastedic.keys():
            dic[food] = tastedic[food]
        else:
            # dic[0] = dic[0] + 1
            # dic[food] = -1
            dic[food] = 0
    return dic

def getModDiningScore(tastedic, eatery):
    taste = getDiningDic(tastedic, eatery)
    # print(taste)
    score = 0;
    total = 0;
    maxval = taste[max(taste, key=taste.get)]
    print(eaterycodes[eatery] + " has")
    for food in taste:
        if(taste[food] == maxval):
            print("   " + str(food))
        sc = getIndexScore(str(food))
        if(sc != -1):
            score = score + sc
            total = total + 1
    print("   " + str(score/total));
    return score/total

def getIndexScore(food):
    with open('data/indexed_taste_data.json', 'r') as fp:
        index = json.load(fp)
    total = 0
    totscore = 0;
    for word in food.split():
        w = word.lower()
        if(w in index):
            if(index[w]["score"] != -1):
                total += 1
                totscore += math.pow(index[w]["score"], 2)
    if(total == 0):
        return 0
    return totscore/total

def getFavoriteFood():
    with open('data/indexed_taste_data.json', 'r') as fp:
        index = json.load(fp)
    m = 0
    maxname = "none"
    for item in index:
        if(index[item]["score"] > m):
            m = index[item]["score"]
            maxname = item
    return m

def getBest():
    with open('data/indexed_taste_data.json', 'r') as fp:
        index = json.load(fp)
    m = 0
    maxname = "none"
    for item in index:
        if(index[item]["score"] == 1.0):
            print(item)

# print(getIndexScore(sys.argv[1]))
# getBest()
# print(getFavoriteFood())
# print(getIndexScore("baKEd Potato with shrimp and onion"))
for x in range(0,1):
    date = time.strftime("%Y-%m-") + str(int(time.strftime("%d")) + x)
    print("\nDate: " + date)
    getBestDining()
