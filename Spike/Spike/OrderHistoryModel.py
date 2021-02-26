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

def getMealList(OrderID):
    myquery = {"OrderID": OrderID}
    orders = mongo.db.OrderHistory.find(myquery)
    result = []
    for order in orders:
        result.append(order["MealID"])
    return result

def getPriority(OrderID):
    myquery = {"OrderID": OrderID}
    orders = mongo.db.OrderHistory.find(myquery)
    order = orders[0]
    return order["Priority"]


def printOrderByPriority():
    orders = mongo.db.OrderHistory.find().sort("Priority", 1)
    result = []
    x = orders[0]["OrderID"]
    count = 0;
    for order in orders:
        print(order)
        if order["OrderID"] == x:
            count += 1
        if count != 2:
            temp = getOrderStatus(order["OrderID"])
            mealList = getMealList(order["OrderID"])
            del order["_id"]
            del order["MealID"]
            order["Status"] = temp
            order["MealIDList"] = mealList
            result.append(order)
        if order["OrderID"] != x:
            x = order["OrderID"]
            count = 0
    return result

def DeleteOrderContentByQuery(Query):
    meal_list = mongo.db.OrderContent
    res = meal_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
