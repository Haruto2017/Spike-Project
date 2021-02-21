from Spike import app, mongo


class OrderContent:
    def __init__(self, OrderID, MealID, Priority):
        self.OrderID = OrderID
        self.MealID = MealID
        self.Priority = Priority

    def insertMeal(self):
        # TODO change table name
        meal_list = mongo.db.Meal
        meal_list.insert_one({'OrderID': self.OrderID, 'MealID': self.MealID, 'Priority': self.Priority})


def DeleteOneMealByQuery(Query):
    meal_list = mongo.db.Meal
    res = meal_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def DeleteManyMealsByQuery(Query):
    meal_list = mongo.db.Meal
    res = meal_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
