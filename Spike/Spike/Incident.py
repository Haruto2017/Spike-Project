from Spike import app, mongo


class Incident:
    def __init__(self, IncidentID, State, Location, Year, Month, Day, Description, Category, streetName):
        self.IncidentID = IncidentID
        # self.State = State
        self.Location = Location
        self.StreetName = streetName
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.Description = Description
        self.Category = Category


def InsertIncident(IncidentID, Location, Description, Category, Year, Month, Day, steerName):
    order_list = mongo.db.Incident
    if findIfIncidentExist(IncidentID) is True:
        return {"Status": False, "Msg": "Incident Has Existed"}
    order_list.insert_one(
        {'IncidentID': IncidentID, 'Location': Location,
         'Description': Description,
         'Category': Category,
         'Year': Year,
         'Month': Month,
         'Day': Day,
         'StreetName': steerName
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
        del x["_id"]
        result.append(x)
    return result


def FindReportsByDate(Year_Start, Month_Start, Day_Start, Year_End, Month_End, Day_End):
    order_list = mongo.db.Incident
    res = order_list.find()
    result = []
    for x in res:

        del x["_id"]
        print(x)
        if int(Year_Start) < int(x["Year"]) < int(Year_End):
            result.append(x)
        elif int(x["Year"]) == int(Year_Start) or int(x["Year"]) == Year_End:
            if int(Month_Start) < int(x["Month"]) < int(Month_End):
                result.append(x)
            elif int(x["Month"] ) == int(Month_Start) or int(x["Month"]) == int(Month_End):
                if int(Day_Start) <= int(x["Day"]) <= int(Day_End):
                    result.append(x)

    return result


def FindReportsByStreet(steerName):
    order_list = mongo.db.Incident
    myquery = {"StreetName": steerName}
    res = order_list.find(myquery)
    result = []
    for x in res:
        del x["_id"]
        result.append(x)
    return result
