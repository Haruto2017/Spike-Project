from Spike import app, mongo


class Meal:
    def __init__(self, MealID, MealName, Picture, Cost, Availability):
        self.MealID = MealID
        self.MealName = MealName
        self.Picture = Picture
        self.Cost = Cost
        self.Availability = Availability

    def insertMeal(self):
        # TODO Change the table name
        meal_list = mongo.db.Meal
        meal_list.insert_one(
            {'MealID': self.MealID, 'MealName': self.MealName, 'Picture': self.Picture, 'Cost': self.Cost,
             'Availability': self.Availability})


def addNewMeal(info_map):
    name = info_map["MealName"]
    picture = info_map["Picture"]
    cost = info_map["Cost"]
    availability = info_map["Availability"]
    meal = Meal("", name, picture, cost, availability)
    meal.insertMeal()
    return True, "Success"


def getMealByID(MealID):
    myquery = {"MealID": MealID}
    meal = mongo.db.Meal.find(myquery)
    return meal[0]["MealName"], meal[0]["Cost"][:-1]


def updateMealInfo(MealName, info_map):
    myquery = {"MealName": MealName}
    newvalues = {"$set": info_map}
    mongo.db.Meal.update_one(myquery, newvalues)
    return True, "Success"


def GetAllItems():
    menu_list = mongo.db.Meal
    res = menu_list.find()
    result = []
    for x in res:
        print(x)
        del x["_id"]
        result.append(x)
    return result


def DeleteOneMealByQuery(Query):
    menu_list = mongo.db.Meal
    res = menu_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def DeleteManyMealsByQuery(Query):
    menu_list = mongo.db.Meal
    res = menu_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
