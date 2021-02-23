# from Spike.OrderModel import Order
#
# order = Order("12345", "JunyuWang", "2019-01-02", "", "", "Incomplete")
# order.insertOrder()
from Spike import mongo
from Spike.OrderHistoryModel import OrderHistory

# order = OrderHistory("12345", "14485", "1", "2021", "2", "12")
# order.insertOrderContent()
info_map = {}
info_map["MealID"] = "12345"
info_map["Year"] = "2021"
info_map["Month"] = "02"
info_map["Day"] = "05"

myquery = {"MealID": "12345"}
# orders = mongo.db.OrderHistory.count_documents({"MealId": "12345"})
orders = mongo.db.OrderHistory.find(info_map).count()
# orders = mongo.db.Meal.find(myquery).count()
print(orders)
