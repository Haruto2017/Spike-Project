"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from Spike import app, mongo
from Spike.MealModel import GetAllItems
from Spike.OrderHistoryModel import CreateOrderHistory, getAllMealByOrderID, printUsageReport, updateOrderHistoryInfo, \
    printOrderByPriority
from Spike.OrderModel import updateOrderInfo, CreateNewOrder, GetOrderHistoryByName, GetOrderHistoryByID, \
    GetAllActiveOrderByName
from Spike.UserModel import ifUserNotExist, create_new_account, verifyAccount, updateUserInfo, getUserInfo
from Spike.MealModel import addNewMeal, updateMealInfo, getMealIDByName


# @app.route('/')
# @app.route('/home')
# def home():
#     """Renders the home page."""
#     return render_template(
#         'index.html',
#         title='Home Page',
#         year=datetime.now().year,
#     )
#


############################ Accounts APIs ###############################
@app.route('/CreateAccount', methods=['GET', 'POST'])
def create_account():
    req = request.get_json()
    status, msg = ifUserNotExist(req["UserName"])
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
    status, msg = verifyAccount(req["UserName"], req["PassWord"])
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


@app.route('/GetAccountInfo', methods=['GET', 'POST'])
def get_account_info():
    req = request.get_json()
    result = getUserInfo(req["UserName"])
    return jsonify(result)


@app.route('/UpdateAccount', methods=['GET', 'POST'])
def update_account():
    req = request.get_json()
    info_map = {}
    UserName = None
    for k in req:
        if k == "UserName":
            UserName = req[k]
        elif k == "PassWord":
            info_map["Password"] = req[k]
        elif k == "Role":
            info_map["Role"] = req[k]
        elif k == "Phone":
            info_map["Phone"] = req[k]
        elif k == "Address":
            info_map["Address"] = req[k]
        elif k == "PaymentType":
            info_map["PaymentType"] = req[k]
    status, msg = updateUserInfo(UserName, info_map)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


##########################################################################


############################ Customer Actions APIs ####################
@app.route('/ViewMenu', methods=['GET', 'POST'])
def view_menu():
    result = GetAllItems()
    return jsonify(result)


@app.route('/CreateOrder', methods=['GET', 'POST'])
def create_order():
    req = request.get_json()
    UserName = req["UserName"]
    foodItems = req["FoodItems"]
    date = req["DateCreated"]
    orderID, year, month, day = CreateNewOrder(UserName, date)
    status = CreateOrderHistory(orderID, year, month, day, foodItems)
    result = {"Status": status, "OrderID": orderID, "Reason": "Order Success"}

    return jsonify(result)


@app.route('/GetOrderHistory', methods=['GET', 'POST'])
def get_order_history():
    req = request.get_json()
    UserName = req["UserName"]
    result = GetOrderHistoryByName(UserName)
    for r in result:
        r["FoodItems"], r["TotalCost"] = getAllMealByOrderID(r["OrderID"])
    return jsonify(result)


@app.route('/GetReceipt', methods=['GET', 'POST'])
def get_receipt():
    req = request.get_json()
    OrderID = req["OrderID"]
    result = GetOrderHistoryByID(OrderID)
    result[0]["FoodItems"], result[0]["TotalCost"] = getAllMealByOrderID(OrderID)
    return jsonify(result)


@app.route('/ViewActiveOrders', methods=['GET', 'POST'])
def view_active_orders():
    req = request.get_json()
    UserName = req["UserName"]
    result = GetAllActiveOrderByName(UserName)
    return jsonify(result)


##########################################################################


######################### Admin Actions APIs #############################

@app.route('/AddItem', methods=['GET', 'POST'])
def add_item():
    req = request.get_json()
    info_map = {}
    for k in req:
        if k == "MealName":
            info_map["MealName"] = req[k]
        elif k == "Picture":
            info_map["Picture"] = req[k]
        elif k == "Cost":
            info_map["Cost"] = req[k]
        elif k == "Availability":
            info_map["Availability"] = req[k]
    status, msg = addNewMeal(info_map)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)


@app.route('/UpdateItem', methods=['GET', 'POST'])
def update_item():
    req = request.get_json()
    info_map = {}
    OriginalName = None
    for k in req:
        if k == "OriginalName":
            OriginalName = req[k]
            info_map["MealName"] = req[k]
        elif k == "NewName":
            info_map["MealName"] = req[k]
        elif k == "Picture":
            info_map["Picture"] = req[k]
        elif k == "Cost":
            info_map["Cost"] = req[k]
        elif k == "Availability":
            info_map["Availability"] = req[k]
    status, msg = updateMealInfo(OriginalName, info_map)
    result = {"Status": status, "Reason": msg}

    return jsonify(result)

@app.route('/UpdateOrder', methods=['GET', 'POST'])
def update_order():
    req = request.get_json()
    OrderID = req["OrderID"]
    info_map = {}
    info_map["Status"] = req["Status"]
    status, msg = updateOrderInfo(OrderID, info_map)
    result = {"Status": status, "Reason": msg}
    return jsonify(result)

@app.route('/UpdateOrderPriority', methods=['GET', 'POST'])
def update_order_priority():
    req = request.get_json()
    OrderID = req["OrderID"]
    info_map = {}
    info_map["Priority"] = req["Priority"]
    status, msg = updateOrderHistoryInfo(OrderID, info_map)
    result = {"Status": status, "Reason": msg}
    return jsonify(result)

@app.route('/PrintOrderByPriority', methods=['GET', 'POST'])
def print_order_by_priority():
    result = printOrderByPriority()
    return jsonify(result)

@app.route('/PrintUsageReport', methods=['GET', 'POST'])
def print_usage_report():
    req = request.get_json()
    info_map = {}
    for k in req:
        if k == "MealName":
            MealID = getMealIDByName(req[k])
            if MealID == False:
                result = {"Status": False, "Reason": "Item is not existed"}
                return jsonify(result)
            info_map["MealID"] = MealID
        elif k == "Year":
            info_map["Year"] = req[k]
        elif k == "Month":
            info_map["Month"] = req[k]
        elif k == "Day":
            info_map["Day"] = req[k]
    status, msg = printUsageReport(info_map)
    result = {"Status": status, "Usage": msg}
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


############################ Restaurant Staff Actions APIs ####################
@app.route('/UpdateMealStock', methods=['GET', 'POST'])
def update_meal_stock():
    req = request.get_json()
    MealName = req["MealName"]
    status = req["InStock"]
    info_map = {}
    if status is True:
        info_map["Availability"] = "Available"
    else:
        info_map["Availability"] = "Unavailable"
    status, msg = updateMealInfo(MealName, info_map)
    result = {"Status": msg}
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
