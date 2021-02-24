from Spike import app, mongo


class Order:
    def __init__(self, OrderID, UserName, CreatedTime, TimetoPickUp, CarDescription, Status):
        self.OrderID = OrderID
        self.UserName = UserName
        self.CreatedTime = CreatedTime
        self.TimetoPickUp = TimetoPickUp
        self.CarDescription = CarDescription
        self.Status = Status

    def insertOrder(self):
        order_list = mongo.db.Order
        order_list.insert_one(
            {'OrderID': self.OrderID, 'UserName': self.UserName, 'CreatedTime': self.CreatedTime,
             'TimetoPickUp': self.TimetoPickUp,
             'CarDescription': self.CarDescription, 'Status': self.Status})


def CreateNewOrder(UserName, CreateTime):
    dates_stamp = CreateTime.split(" ")
    dates = dates_stamp[0].split("-")
    year, month, day = dates[0], dates[1], dates[2]
    orderID = UserName + CreateTime
    order = Order(orderID, UserName, CreateTime, "", "", "Incomplete")
    order.insertOrder()

    return orderID, year, month, day


def GetOrderHistoryByName(UserName):
    myquery = {"UserName": UserName}
    orders = mongo.db.Order.find(myquery)
    result = []
    for order in orders:
        del order["_id"]
        result.append(order)
    return result


def GetAllActiveOrderByName(UserName):
    myquery = {"UserName": UserName, "Status": "Incomplete"}
    orders = mongo.db.Order.find(myquery)
    result = []
    for order in orders:
        result.append(order["OrderID"])
    return result


def GetOrderHistoryByID(OrderID):
    myquery = {"OrderID": OrderID}
    orders = mongo.db.Order.find(myquery)
    result = []
    for order in orders:
        del order["_id"]
        result.append(order)
    return result


def updateOrderInfo(OrderID, infoMap):
    myquery = {"OrderID": OrderID}
    newvalues = {"$set": infoMap}
    mongo.db.Order.update_one(myquery, newvalues)
    return True, "Success"

def getOrderStatus(OrderID):
    myquery = {"OrderID": OrderID}
    orders = mongo.db.Order.find(myquery)
    order = orders[0]
    return order["Status"]

def DeleteOneOrderByQuery(Query):
    order_list = mongo.db.Order
    res = order_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def updateAllOrderUserName(OldName, NewName):
    myquery = {"UserName": OldName}
    info_map = {"UserName": NewName}
    newvalues = {"$set": info_map}
    mongo.db.Order.update_many(myquery, newvalues)
    return


def DeleteManyOrdersByQuery(Query):
    order_list = mongo.db.Order
    res = order_list.delete_many(Query)
    return True, "Success delete {} items".format(res.deleted_count)
