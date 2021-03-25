from Spike import app, mongo


class Incident:
    def __init__(self, IncidentID, State, Location, Year, Month, Day, Description, Category, steerName):
        self.IncidentID = IncidentID
        self.State = State
        self.Location = Location
        self.steerName = steerName
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.Description = Description
        self.Category = Category


def InsertIncident(IncidentID, State, Location, Description, Category, Year, Month, Day, steerName):
    order_list = mongo.db.Incident
    if findIfIncidentExist(IncidentID) is True:
        return {"Status": False, "Msg": "Incident Has Existed"}
    order_list.insert_one(
        {'IncidentID': IncidentID, 'State': State, 'Location': Location,
         'Description': Description,
         'Category': Category,
         'Year': Year,
         'Month': Month,
         'Day': Day,
         'steerName': steerName
         })
    return {"Status": True, "Msg": "Success"}

def findIfIncidentExist(IncidentID):
    order_list = mongo.db.Incident
    myquery = {"IncidentID": IncidentID}
    users = order_list.find(myquery)
    length = users.count()
    if length > 0:
        return True
    return False


def DeleteIncidentById(IncidentID):
    order_list = mongo.db.Incident
    myquery = {"IncidentID": IncidentID}
    if findIfIncidentExist(IncidentID) is False:
        return {"Status": False, "Msg": "Incident Does Not Exist"}
    order_list.delete_one(myquery)
    result = {"Status": True, "Msg": "Success"}
    return result


def FindByCategory(Category):
    order_list = mongo.db.Incident
    myquery = {"Category": Category}
    res = order_list.find(myquery)
    result = []
    for x in res:
        result.append(x)
    return result

def FindReportsByDate(Year, Month, Day):
    order_list = mongo.db.Incident
    myquery = {"Year": Year, "Month": Month, "Day": Day}
    res = order_list.find(myquery)
    result = []
    for x in res:
        result.append(x)
    return result

def FindReportsByStreet(steerName):
    order_list = mongo.db.Incident
    myquery = {"steerName": steerName}
    res = order_list.find(myquery)
    result = []
    for x in res:
        result.append(x)
    return result