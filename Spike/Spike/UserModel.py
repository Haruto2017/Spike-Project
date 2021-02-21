from Spike import app, mongo


class User:
    def __init__(self, UserID="", UserName="", Role="", PaymentType="", PassWord="", Phone="", Address=""):
        self.UserID = UserID
        self.UserName = UserName
        self.Role = Role
        self.PaymentType = PaymentType
        self.PassWord = PassWord
        self.Phone = Phone
        self.Address = Address

    def insertUser(self):
        user_list = mongo.db.User
        user_list.insert_one(
            {'UserID': self.UserID, 'UserName': self.UserName, 'Role': self.Role, 'PaymentType': self.PaymentType,
             'Password': self.PassWord, 'Phone': self.Phone, 'Address': self.Address})


def create_new_account(info_map):
    userName = info_map["Username"]
    passWord = info_map["Password"]
    phone = info_map["Phone"]
    role = info_map["Role"]
    address = info_map["Address"]
    user = User("", userName, role, "", passWord, phone, address)
    user.insertUser()
    return True, "Success"


def updateUserInfo(UserName, infoMap):
    myquery = {"UserName": UserName}
    newvalues = {"$set": infoMap}
    mongo.db.User.update_one(myquery, newvalues)
    return True, "Success"



def getUserInfo(UserName):
    myquery = {"UserName": UserName}
    users = mongo.db.User.find(myquery)

    length = users.count()
    if length <= 0:
        return {'UserName': "", 'Role': "",
                'PaymentType': "",
                'Phone': "", 'Address': "",
                "Reason": "UserName not Exist", "Status": False}
    user = users[0]
    result = {"UserName": user["UserName"], "Role": user["Role"], "PaymentType": user["PaymentType"],
              "Phone": user["Phone"], "Address": user["Address"],
              "Reason": "success", "Status": True}


    return result


def ifUserNotExist(UserName):
    # While creating a new account, check whether a UserName has existed
    myquery = {"UserName": UserName}
    users = mongo.db.User.find(myquery)
    length = users.count()
    if length > 0:
        return False, "UserName has Exist"
    return True, "Success"


def verifyAccount(UserName, PassWord):
    myquery = {"UserName": UserName}
    users = mongo.db.User.find(myquery)
    length = users.count()
    if length < 1:
        return False, "User Not Exist"
    if length > 1:
        return False, "Duplicated User"
    if users[0]["Password"] != PassWord:
        return False, "Wrong PassWord"
    return True, "Success"


def DeleteOneUserByQuery(UserName, PassWord):
    status, msg = verifyAccount(UserName, PassWord)
    if status is False:
        return False, msg
    myquery = {"UserName": UserName}
    user_list = mongo.db.User
    user_list.delete_one(myquery)
    return True, "Success"

# Currently no such function
# def DeleteManyUsersByQuery(Query):
#     user_list = mongo.db.User
#     res = user_list.delete_many(Query)
#     return res.deleted_count
