"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from Spike import app, mongo
from Spike.UserModel import ifUserNotExist, create_new_account, verifyAccount, updateUserInfo


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


############################ Accounts APIs ###############################
@app.route('/CreateAccount', method=['POST'])
def create_account():
    req = request.get_json()
    status, msg = ifUserNotExist(req["Username"])
    result = {"Status": status, "Reason": msg}
    if status is False:
        return jsonify(result)
    status, msg = create_new_account(req)
    result["Status"] = status
    result["Reason"] = msg
    return jsonify(result)


@app.route('/VerifyAccount')
def verify_account():
    req = request.get_json()
    status, msg = verifyAccount(req["Username"], req["Password"])
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


@app.route('/UpdateAccount')
def update_account():
    req = request.get_json()
    info_map = {}
    userName = None
    for k in req:
        if k == "Username":
            userName = req[k]
        elif k == "Password":
            info_map["PassWord"] = req[k]
        elif k == "Role":
            info_map["Role"] = req[k]
        elif k == "Phone":
            info_map["Phone"] = req[k]
        elif k == "Address":
            info_map["Address"] = req[k]
        elif k == "PaymentType":
            info_map["PaymentType"] = req[k]
    status, msg = updateUserInfo(userName, info_map)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


##########################################################################


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
