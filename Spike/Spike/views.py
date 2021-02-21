"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from Spike import app, mongo
from Spike.MealModel import GetAllItems
from Spike.OrderModel import updateOrderInfo
from Spike.UserModel import ifUserNotExist, create_new_account, verifyAccount, updateUserInfo, getUserInfo
from Spike.MealModel import addNewMeal, updateMealInfo


# @app.route('/')
# @app.route('/home')
# def home():
#     """Renders the home page."""
#     return render_template(
#         'index.html',
#         title='Home Page',
#         year=datetime.now().year,
#     )


############################ Accounts APIs ###############################
@app.route('/CreateAccount', methods=['GET', 'POST'])
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


@app.route('/VerifyAccount', methods=['GET', 'POST'])
def verify_account():
    req = request.get_json()
    status, msg = verifyAccount(req["Username"], req["Password"])
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


@app.route('/GetAccountInfo', methods=['GET', 'POST'])
def get_account_info():
    req = request.get_json()
    result = getUserInfo(req["Username"])
    return jsonify(result)


@app.route('/UpdateAccount',  methods = ['GET', 'POST'])
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
######################### Admin Actions APIs #############################

@app.route('/AddItem', methods=['GET', 'POST'])
def add_item():
    req = request.get_json()
    info_map = {}
    for k in req:
        if k == "Name":
            info_map["Name"] = req[k]
        elif k == "Picture":
            info_map["Picture"] = req[k]
        elif k == "Cost":
            info_map["Cost"] = req[k]
        elif k == "Availability":
            info_map["Availability"] = req[k]
    status, msg = addNewMeal(req)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)

@app.route('/UpdateItem', methods=['GET', 'POST'])
def update_item():
    req = request.get_json()
    info_map = {}
    mealName = None
    for k in req:
        if k == "Name":
            info_map["Name"] = req[k]
        elif k == "Picture":
            info_map["Picture"] = req[k]
        elif k == "Cost":
            info_map["Cost"] = req[k]
        elif k == "Availability":
            info_map["Availability"] = req[k]
    status, msg = updateMealInfo(mealName, req)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


##########################################################################

############################ Customer Actions APIs ####################
@app.route('/ViewMenu', methods=['GET', 'POST'])
def view_menu():
    result = GetAllItems()
    return jsonify(result)


##########################################################################



############################ Pick Up Information APIs ####################
@app.route('/AddPickUpInfo', methods=['GET', 'POST'])
def add_pick_up_info():
    req = request.get_json()
    order_id = req["OrderID"]
    status, msg = updateOrderInfo(order_id, req)
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



@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
