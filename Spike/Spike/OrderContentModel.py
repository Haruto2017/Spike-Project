from Spike import app, mongo


class OrderContent:
    def __init__(self, OrderID, MealID, Priority):
        self.OrderID = OrderID
        self.MealID = MealID
        self.Priority = Priority

    def insertOrderContent(self):
        orderContent_list = mongo.db.OrderContent
        orderContent_list.insert_one({'OrderID': self.OrderID, 'MealID': self.MealID, 'Priority': self.Priority})


def DeleteOrderContentByQuery(Query):
    meal_list = mongo.db.OrderContent
    res = meal_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
