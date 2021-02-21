from Spike import app, mongo


class OrderHistory:
    def __init__(self, OrderID, MealID, Priority, Year, Month, Day):
        self.OrderID = OrderID
        self.MealID = MealID
        self.Priority = Priority
        self.Year = Year
        self.Month = Month
        self.Day = Day

    def insertOrderContent(self):
        orderContent_list = mongo.db.OrderHistory
        orderContent_list.insert_one({'OrderID': self.OrderID, 'MealID': self.MealID, 'Priority': self.Priority, "Year": self.Year, "Month": self.Month, "Day": self.Day})


def DeleteOrderContentByQuery(Query):
    meal_list = mongo.db.OrderContent
    res = meal_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
