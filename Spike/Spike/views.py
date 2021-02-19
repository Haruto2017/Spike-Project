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
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
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
