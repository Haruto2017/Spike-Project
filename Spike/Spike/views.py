"""
Routes and views for the flask application.
"""

from flask import render_template, jsonify, request
from Spike import app, mongo
from Spike.Incident import InsertIncident, DeleteIncidentById, FindByCategory, FindReportsByDate, FindReportsByLocation


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

    steerName = req.get("StreetName")
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
    Category = req.get("Category")
    if Category is None:
        return jsonify(result)
    result = InsertIncident(IncidentID, Location, Description, Category, Year, Month, Day, steerName)
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
    BeginYear = req.get("BeginYear")
    if BeginYear is None:
        return jsonify(result)
    BeginMonth = req.get("BeginMonth")
    if BeginMonth is None:
        return jsonify(result)
    BeginDay = req.get("BeginDay")
    if BeginDay is None:
        return jsonify(result)
    EndYear = req.get("EndYear")
    if EndYear is None:
        return jsonify(result)
    EndMonth = req.get("EndMonth")
    if EndMonth is None:
        return jsonify(result)
    EndDay = req.get("EndDay")
    if BeginDay is None:
        return jsonify(result)
    data = FindReportsByDate(BeginYear, BeginMonth, BeginDay, EndYear, EndMonth, EndDay)
    result= {"Status": True, "Msg": "Success", "Data": data}
    return jsonify(result)


@app.route('/getReportByLocation', methods=('GET', 'POST'))
def getReportByLocation():
    result = {"Status": False, "Msg": "Date is lack of information", "Data": []}
    req = request.get_json()
    longitude = req.get("longitude")
    if longitude is None:
        return jsonify(result)
    latitude = req.get("latitude")
    if latitude is None:
        return jsonify(result)
    longitudeDelta = req.get("longitudeDelta")
    if longitudeDelta is None:
        return jsonify(result)
    latitudeDelta = req.get("latitudeDelta")
    if latitudeDelta is None:
        return jsonify(result)

    data = FindReportsByLocation(longitude,latitude,longitudeDelta,latitudeDelta)
    result = {"Status": True, "Msg": "Success", "Data": data}
    return jsonify(result)


