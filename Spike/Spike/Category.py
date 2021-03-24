from Spike import app, mongo

class Incident:
    def __init__(self, IncidentID, Category):
        self.IncidentID = IncidentID
        self.Category = Category

    def insertIncident(self):
        order_list = mongo.db.Category
        order_list.insert_one(
            {'IncidentID': self.IncidentID, 'Category' : self.Category})