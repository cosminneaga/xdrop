from flask import request
import os

from handlers.admin import AdminHandler
from handlers.response import ResponseHandler
from handlers.auth import AdminAuthHandler
from helpers import HelperErrorToTXT



class AdminController:

    def login(data):
        login = AdminHandler.login(data)
        if login:
            return login
        return ResponseHandler.error_success_handler('Username/password does not match with our records.', True, False, 'ADMIN_CREDENTIALS_ERROR_USR_NOTFOUND'), 400

    def getAllLicences(token):
        try: 
            AdminAuthHandler.checkIfAuthorized(token)
            return { "licences": AdminHandler.getLicences() }
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' getAllLicences()')
            return '', 400

    def getLicencesNumber(token):
        try: 
            AdminAuthHandler.checkIfAuthorized(token)
            getNumber = AdminHandler.getLicencesNumber()
            return { "no": getNumber }
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' getLicencesNumber()')
            return {'success': False, 'authorization': token}, 400

    def createLicence(token, data):
        try:
            AdminAuthHandler.checkIfAuthorized(token)
            generatedLicence = AdminHandler.createLicence(data)
            return ResponseHandler.error_success_handler(generatedLicence, False, True, 'LICENCE_GENERATED')
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' createLicence()')
            return '', 400

    def extendLicence(token, data):
        try: 
            AdminAuthHandler.checkIfAuthorized(token)
            extend = AdminHandler.extendLicence(data)
            return {'success': True, 'message': 'Licence extended.'}
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' extendLicence()')
            return '', 400

    def getDefaultMessages(token):
        try:
            AdminAuthHandler.checkIfAuthorized(token)
            messages = AdminHandler.getDefaultMessages()
            return messages
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' getDefaultMessages()')
            return '', 400
    
    def setDefaultMessages(token, data):
        try:
            AdminAuthHandler.checkIfAuthorized(token)
            AdminHandler.setDefaultMessages(data)
            return {
                'success': True,
                'message': 'Default messages updated.'
            }
        except Exception as e:
            HelperErrorToTXT.write('admin', e, request, os.path.relpath(__file__) + ' setDefaultMessages()')
            return '', 400
