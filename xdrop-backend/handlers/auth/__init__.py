import jwt
import os
from datetime import datetime
from sys import platform
from helpers import HelperErrorToTXT
from handlers.env import EnvironmentHandler
from handlers.db import DBHandler

colLicences = DBHandler.getDBCollection('licences')
colAdmin = DBHandler.getDBCollection('administrator')
sessionPath = EnvironmentHandler.getSessionPath()
jwtOpt = EnvironmentHandler.getJWTOptions()

class AdminAuthHandler():

    def checkUserAgainstDB(username, password):
        search = list(colAdmin.find({"username": username}))
        if len(search) == 1:
            if search[0]["password"] == password:
                return True
        return False

    def checkIfAuthorized(jwtString):
        if not jwtString:
            return False
        jwtString = jwtString.split(' ')[1]
        user = jwt.decode(jwtString, jwtOpt['adminSecret'], jwtOpt['algorithm'])
        return AdminAuthHandler.checkUserAgainstDB(user['username'], user['password'])

    def setSessionKey(username, password):
        check = AdminAuthHandler.checkUserAgainstDB(username, password)
        if check:
            encoded = jwt.encode({ "username": username, "password": password }, jwtOpt['adminSecret'], jwtOpt['algorithm'])
            if platform == "linux" or platform == "linux2":
                return {"token": encoded.decode('UTF-8')}
            return {"token": encoded}
        return False



class UserAuthHandler():

    def checkLicenceAgainstDB(licence):
        search = colLicences.find_one({"key": licence})
        if search and search["validity"] > datetime.now():
            return True
        return False

    def checkLicenceIfAuthorized(token):
        if not token:
            return False
        token = token.split(' ')[1]
        try:
            licence = jwt.decode(token, jwtOpt['userSecret'], jwtOpt['algorithm'])
            return UserAuthHandler.checkLicenceAgainstDB(licence['licence'])
        except Exception as e:
            HelperErrorToTXT.write('user_jwt_error', e, '', os.path.relpath(__file__) + 'UserHandler.checkLicenceIfAuthorized()')
            return False

    def setLicenceSessionKey(licence):
        encoded = jwt.encode({"licence": licence}, jwtOpt['userSecret'], jwtOpt['algorithm'])
        if platform == "linux" or platform == "linux2":
            return {"token": encoded.decode('UTF-8')}
        return {"token": encoded}

    def decodeLicenceJWT(token):
        token = token.split(' ')[1]
        try:
            return jwt.decode(token, jwtOpt['userSecret'], jwtOpt['algorithm'])['licence']
        except Exception as e:
            HelperErrorToTXT.write('user_jwt_error', e, '',  os.path.relpath(__file__) + os.path.relpath(__file__) + 'UserHandler.decodeLicenceJWT()')
            return False

    def checkIfLicenceStatusIsOnline(licence):
        find = colLicences.find_one({
            'key': licence
        },{
            '_id': 0,
            'online': 1
        })
        return find['online']