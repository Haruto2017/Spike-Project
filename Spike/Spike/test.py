# from Spike.OrderModel import Order
#
# order = Order("12345", "JunyuWang", "2019-01-02", "", "", "Incomplete")
# order.insertOrder()
from Spike import mongo
from Spike.OrderHistoryModel import OrderHistory

# order = OrderHistory("12345", "14485", "1", "2021", "2", "12")
# order.insertOrderContent()
MealName = "YAKI SOB"
myquery = {"MealName": MealName}
meal = mongo.db.Meal.find(myquery)
c = meal.count()
print(meal,c)
