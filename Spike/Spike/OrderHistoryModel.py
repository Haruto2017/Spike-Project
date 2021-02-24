from Spike import app, mongo
from Spike.MealModel import getMealByID
from Spike.OrderModel import getOrderStatus


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
        orderContent_list.insert_one(
            {'OrderID': self.OrderID, 'MealID': self.MealID, 'Priority': self.Priority, "Year": self.Year,
             "Month": self.Month, "Day": self.Day})

def printUsageReport(info_map):
    usage = mongo.db.OrderHistory.count_documents(info_map)
    return True, usage

def getAllMealByOrderID(OrderID):
    myquery = {"OrderID": OrderID}
    mealNameList = []
    moneyNum = 0
    orders = mongo.db.OrderHistory.find(myquery)
    for order in orders:
        meal_name, money = getMealByID(order["MealID"])
        mealNameList.append(meal_name)
        moneyNum += float(money)
    return mealNameList, str(moneyNum) + "$"

def CreateOrderHistory(OrderID, Year, Month, Day, foodItems):
    for foodID in foodItems:
        orderHis = OrderHistory(OrderID, foodID, "3", Year, Month, Day)
        orderHis.insertOrderContent()
    return True

def updateOrderHistoryInfo(OrderID, info_map):
    myquery = {"OrderID": OrderID}
    newvalues = {"$set": info_map}
    mongo.db.OrderHistory.update_one(myquery, newvalues)
    return True, "Success"



def printOrderByPriority():
    orders = mongo.db.OrderHistory.find().sort("Priority", 1)
    result = []
    for order in orders:
        print(order)
        temp = getOrderStatus(order["OrderID"])
        del order["_id"]
        order["Status"] = temp
        result.append(order)
    return result

def DeleteOrderContentByQuery(Query):
    meal_list = mongo.db.OrderContent
    res = meal_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
