from handlers.db import DBHandler

colLicence = DBHandler.getDBCollection('licences')
colApp = DBHandler.getDBCollection('app')

class UserGeneralHandler:

    def getProfileData(token):
        data = colLicence.find_one({'key': token})
        return {
            'licence': data['key'],
            'validity': data['validity'],
            'plan': data['plan'],
            'created': data['created_on']
        }

    def getVersion(token):
        data = colApp.find_one({'_id': 1})
        return {
            'version': data['version']
        }