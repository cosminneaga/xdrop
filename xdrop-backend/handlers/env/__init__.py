import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class EnvironmentHandler():

    def getEnvs():
        object = {}
        if os.getenv('ENV') == 'prod':
            object['port'] = os.getenv('PORT_PROD')
            object['db_client'] = os.getenv('DB_PROD')
        elif os.getenv('ENV') == 'dev':
            object['port'] = os.getenv('PORT_DEV')
            object['db_client'] = os.getenv('DB_DEV')

        return object

    def getDbName():
        return os.getenv('DB_NAME')

    def getSessionPath():
        return os.getenv('TELEGRAM_SESSIONS_PATH')

    def getJWTOptions():
        return {
            'adminSecret': os.getenv('JWT_SECRET_ADMIN'),
            'userSecret': os.getenv('JWT_SECRET_USER'),
            'algorithm': os.getenv('JWT_ALGORITHM')
        }