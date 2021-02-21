from Spike import app, mongo


class Meal:
    def __init__(self, MealID, MealName, Picture, Cost, Availability):
        self.MealID = MealID
        self.MealName = MealName
        self.Picture = Picture
        self.Cost = Cost
        self.Availability = Availability

    def insertMenu(self):
        # TODO Change the table name
        # TODO change the Availability spelling
        menu_list = mongo.db.Menu
        menu_list.insert_one(
            {'MealID': self.MealID, 'MealName': self.MealName, 'Picture': self.Picture, 'Cost': self.Cost,
             'Availability': self.Availability})

def addNewMeal(info_map):
    name = info_map["Name"]
    picture = info_map["Picture"]
    cost = info_map["Cost"]
    avaibility = info_map["Availability"]
    meal = Meal("", picture, cost,avaibility)
    meal.insertMenu()
    return True, "Success"

def DeleteOneMenuByQuery(Query):
    menu_list = mongo.db.Menu
    res = menu_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def DeleteManyMenusByQuery(Query):
    menu_list = mongo.db.Menu
    res = menu_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
