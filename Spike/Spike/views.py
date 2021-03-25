"""
Routes and views for the flask application.
"""

from flask import render_template, jsonify, request
from Spike import app, mongo
from Spike.Incident import InsertIncident, DeleteIncidentById, FindByCategory, FindReportsByDate


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
# IncidentID, State, Location, Date, Description, Category
@app.route('/reportCreate', methods=('GET', 'POST'))
def report_create():
    req = request.get_json()
    result = {"Status": False, "Msg": "Report is lack of information"}
    IncidentID = req.get("IncidentID")
    if IncidentID is None:
        return jsonify(result)

    State = req.get("State")
    if State is None:
        return jsonify(result)
    steerName = req.get("steerName")
    if steerName is None:
        return jsonify(result)
    Location = req.get("Location")
    if Location is None:
        return jsonify(result)
    Year = req.get("Year")
    if Year is None:
        return jsonify(result)
    Month = req.get("Month")
    if Month is None:
        return jsonify(result)
    Day = req.get("Day")
    if Day is None:
        return jsonify(result)
    Description = req.get("Description")
    if Description is None:
        return jsonify(result)
    Category = req.get("Description")
    if Category is None:
        return jsonify(result)
    result = InsertIncident(IncidentID, State, Location, Description, Category, Year, Month, Day, steerName)
    return jsonify(result)


@app.route('/deleteReportByID', methods=('GET', 'POST'))
def delete():
    req = request.get_json()
    result = {"Status": False, "Msg": "Need a IncidentId to delete"}
    IncidentID = req.get("IncidentID")
    if IncidentID is None:
        return jsonify(result)
    result = DeleteIncidentById(IncidentID)
    return jsonify(result)


@app.route('/getReportByCategory', methods=('GET', 'POST'))
def getReportByCategory():
    req = request.get_json()
    result = {"Status": False, "Msg": "Need a Category to search"}
    Category = req.get("Category")
    if Category is None:
        return jsonify(result)
    result = FindByCategory(Category)
    return jsonify(result)


@app.route('/getReportByDate', methods=('GET', 'POST'))
def getReportByDate():
    result = {"Status": False, "Msg": "Date is lack of information"}
    req = request.get_json()
    Year = req.get("Year")
    if Year is None:
        return jsonify(result)
    Month = req.get("Month")
    if Month is None:
        return jsonify(result)
    Day = req.get("Day")
    if Day is None:
        return jsonify(result)
    FindReportsByDate(Year, Month, Day)
    result = {"Status": True, "Msg": "Success"}
    return jsonify(result)


@app.route('/getReportByLocation', methods=('GET', 'POST'))
def getReportByLocation():
    result = {"Status": False, "Msg": "Date is lack of information"}
    req = request.get_json()
    steerName = req.get("steerName")
    if steerName is None:
        return jsonify(result)

    FindReportsByDate(steerName)
    result = {"Status": True, "Msg": "Success"}
    return jsonify(result)


