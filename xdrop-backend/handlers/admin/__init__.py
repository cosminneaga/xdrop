from handlers.db import DBHandler
from handlers.auth import AdminAuthHandler
from datetime import datetime, timedelta
from helpers import GenerateRandomStringAgainstDB

colLicences = DBHandler.getDBCollection('licences')
colMessages = DBHandler.getDBCollection('default_messages')

class AdminHandler():

    def login(data):
        authorise = AdminAuthHandler.setSessionKey(data['id'], data['password'])
        if authorise:
            return authorise
        return False

    def getLicences():
        group = colLicences.find()
        data = []
        for licence in group:
            data.append({
            "licence": licence['key'],
            "validity": licence['validity'],
            "plan": licence['plan'],
            "created_on": licence['created_on'],
            "online": licence['online']
            })
        return data

    def getLicencesNumber():
        return colLicences.find().count()

    def extendLicence(obj):
        licence = colLicences.find_one({"key": obj['licence']})
        newValueValidity = licence["validity"] + timedelta(days=obj["days"]) + timedelta(hours=obj["hours"])
        colLicences.update_one({"key": obj["licence"]}, {
            "$set": {"validity": newValueValidity}
        })

    def createLicence(obj):
        licenceArr = colLicences.find({}, {"_id": 0, "key": 1})
        licenceList = []
        for x in licenceArr:
            licenceList.append(x['key'])
        generatedLicence = GenerateRandomStringAgainstDB.generateRandomUniqueStrings(60, licenceList)
        colLicences.insert_one({
            "key": generatedLicence,
            "validity": datetime.now() + timedelta(days=obj["days"]) + timedelta(hours=obj["hours"]),
            "plan": obj['plan'],
            "created_on": datetime.now(),
            "online": False
        })
        return generatedLicence

    def getDefaultMessages():
        messages = list(colMessages.find({}, {"_id": 0}))
        return {
            "regular": messages[0]["regular"],
            "free": messages[0]["free"]
        }

    def setDefaultMessages(obj):
        colMessages.update({}, {
            "$set": {
                "free": obj["free"],
                "regular": obj["regular"]
            }
        })
        return True