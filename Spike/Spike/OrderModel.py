from Spike import app, mongo


class Order:
    def __init__(self, OrderID, UserID, CreatedTime, TimetoPickUp, CarDescription, Status):
        self.OrderID = OrderID
        self.UserID = UserID
        self.CreatedTime = CreatedTime
        self.TimetoPickUp = TimetoPickUp
        self.CarDescription = CarDescription
        self.Status = Status

    def insertOrder(self):
        order_list = mongo.db.Order
        order_list.insert_one(
            {'OrderID': self.OrderID, 'UserID': self.UserID, 'CreatedTime': self.CreatedTime,
             'TimetoPickUp': self.TimetoPickUp,
             'CarDescription': self.CarDescription, 'Status': self.Status})


def updateOrderInfo(OrderID, infoMap):
    myquery = {"OrderID": OrderID}
    newvalues = {"$set": infoMap}
    mongo.db.Order.update_one(myquery, newvalues)
    return True, "Success"


def DeleteOneOrderByQuery(Query):
    order_list = mongo.db.Order
    res = order_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def DeleteManyOrdersByQuery(Query):
    order_list = mongo.db.Order
    res = order_list.delete_many(Query)
    return True, "Success delete {} items".format(res.deleted_count)
