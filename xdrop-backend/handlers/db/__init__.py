import pymongo
from handlers.env import EnvironmentHandler 

dbConnString = EnvironmentHandler.getEnvs()['db_client']
dbName = EnvironmentHandler.getDbName()

class DBHandler():

    def getDBClient():
        return pymongo.MongoClient(dbConnString)[dbName]

    def getDBCollection(colName):
        return pymongo.MongoClient(dbConnString)[dbName][colName]