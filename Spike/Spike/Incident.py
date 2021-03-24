from Spike import app, mongo

class Incident:
    def __init__(self, IncidentID, State, Location, Date, Description):
        self.IncidentID = IncidentID
        self.State = State
        self.Location = Location
        self.Date = Date
        self.Description = Description

    def insertIncident(self):
        order_list = mongo.db.Incident
        order_list.insert_one(
            {'IncidentID': self.IncidentID, 'State': self.State, 'Location': self.Location,
             'Date': self.Date,
             'Description': self.Description})