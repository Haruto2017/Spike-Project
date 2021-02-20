"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify
from Spike import app, mongo

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    testUser = User(12, "Mike", "Customer", "Credit", "abc", 12522, "West Ave")
    testUser.insertUser()
    testOrder = Order(12, 12, 123, 1234, "Toyota", "completed")
    testOrder.insertOrder()
    testMeal = Meal(12, 143, 222)
    testMeal.insertMeal()
    testMenu = Menu(12, "asasa", 1212, 12123, "yes")
    testMenu.insertMenu()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/ViewMenu')
def view_menu():
    """Renders the contact page."""
    result = {}
    food_items = [["12343", "dish1", "imageUrl1", "10", "Available"],
                  ["12452", "dish2", "imageUrl2", "24", "Unavailable"]]
    result["Menu"] = food_items
    result["Length"] = len(food_items)
    return jsonify(result)


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


class User:
    def __init__(self, UserID, UserName, Role, PaymentType, PassWord, Phone, Address):
        self.UserID = UserID
        self.UserName = UserName
        self.Role = Role
        self.PaymentType = PaymentType
        self.PassWord = PassWord
        self.Phone = Phone
        self.Address = Address

    def insertUser(self):
        user_list = mongo.db.User
        user_list.insert_one(
            {'UserID': self.UserID, 'UserName': self.UserName, 'Role': self.Role, 'PaymentType': self.PaymentType,
             'Password': self.PassWord, 'Phone': self.Phone, 'Address': self.Address})

    def DeleteOneUserByQuery(Query):
        user_list = mongo.db.User
        res = user_list.delete_one(Query)
        return res.deleted_count

    def DeleteManyUsersByQuery(Query):
        user_list = mongo.db.User
        res = user_list.delete_many(Query)
        return res.deleted_count


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
            {'OrderID': self.OrderID, 'UserID': self.UserID, 'CreatedTime': self.CreatedTime, 'TimetoPickUp': self.TimetoPickUp,
             'CarDescription': self.CarDescription, 'Status': self.Status})

    def DeleteOneOrderByQuery(Query):
        order_list = mongo.db.Order
        res = order_list.delete_one(Query)
        return res.deleted_count

    def DeleteManyOrdersByQuery(Query):
        order_list = mongo.db.Order
        res = order_list.delete_many(Query)
        return res.deleted_count

class Meal:
    def __init__(self, OrderID, MealID, Priority):
        self.OrderID = OrderID
        self.MealID = MealID
        self.Priority = Priority

    def insertMeal(self):
        meal_list = mongo.db.Meal
        meal_list.insert_one({'OrderID': self.OrderID, 'MealID': self.MealID, 'Priority': self.Priority})

    def DeleteOneMealByQuery(Query):
        meal_list = mongo.db.Meal
        res = meal_list.delete_one(Query)
        return res.deleted_count

    def DeleteManyMealsByQuery(Query):
        meal_list = mongo.db.Meal
        res = meal_list.delete_many(Query)
        return res.deleted_count

class Menu:
    def __init__(self, MealID, MealName, Picture, Cost, Avaibility):
        self.MealID = MealID
        self.MealName = MealName
        self.Picture = Picture
        self.Cost = Cost
        self.Avaibility = Avaibility

    def insertMenu(self):
        menu_list = mongo.db.Menu
        menu_list.insert_one({'MealID': self.MealID, 'MealName': self.MealName, 'Picture': self.Picture, 'Cost': self.Cost, 'Avaibility': self.Avaibility})

    def DeleteOneMenuByQuery(Query):
        menu_list = mongo.db.Menu
        res = menu_list.delete_one(Query)
        return res.deleted_count

    def DeleteManyMenusByQuery(Query):
        menu_list = mongo.db.Menu
        res = menu_list.delete_many(Query)
        return res.deleted_count