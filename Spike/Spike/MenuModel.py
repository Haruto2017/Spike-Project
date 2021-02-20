from Spike import app, mongo


class Menu:
    def __init__(self, MealID, MealName, Picture, Cost, Avaibility):
        self.MealID = MealID
        self.MealName = MealName
        self.Picture = Picture
        self.Cost = Cost
        self.Avaibility = Avaibility

    def insertMenu(self):
        menu_list = mongo.db.Menu
        menu_list.insert_one(
            {'MealID': self.MealID, 'MealName': self.MealName, 'Picture': self.Picture, 'Cost': self.Cost,
             'Avaibility': self.Avaibility})


def DeleteOneMenuByQuery(Query):
    menu_list = mongo.db.Menu
    res = menu_list.delete_one(Query)
    return True, "Success delete {} item".format(res.deleted_count)


def DeleteManyMenusByQuery(Query):
    menu_list = mongo.db.Menu
    res = menu_list.delete_many(Query)
    return True, "Success delete {} item".format(res.deleted_count)
