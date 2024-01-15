import os
from flask import request


from handlers.auth import UserAuthHandler
from handlers.response import ResponseHandler
from handlers.env import EnvironmentHandler
from handlers.telethon import UserHandler
from handlers.user import UserGeneralHandler

from helpers import HelperErrorToTXT

sessions_path = EnvironmentHandler.getSessionPath()


message_licence_online_error = "The licence you trying to use has already a session running on our server.\n You will not be able to use the same sessions on two different devices at the same time."
message_invalid_licence = "The licence entered has not been validated or has been expired."
message_token_invalidated = 'Your token string has been invalidated. Try to logout and login in again.'
message_not_authorized = 'Your token has not been authorized to access this route. \nMost likely this error pops up because your licence has been expired. \nPlease contact administrator regarding this error.'
message_error_fields_empty = "The fields must be not empty..."


class UserController:

    # @protected false
    # @route /api/login 
    # @methods POST
    # @params licence: string
    # @desc used to login user into XDropPro
    def login(licence):
        isOnline = False
        try:
            checkLicence = UserAuthHandler.checkLicenceAgainstDB(licence)
            if not checkLicence:
                raise ValueError(message_invalid_licence)

            online = UserAuthHandler.checkIfLicenceStatusIsOnline(licence)
            if online:
                isOnline = True
                raise ValueError(message_licence_online_error)
            
            UserHandler.setLicenceOnlineStatus(licence, True)
            return UserHandler.login(licence)
                
        except Exception as e:
            HelperErrorToTXT.write('user_login_general_error', e, request, os.path.relpath(__file__) + ' login()')
            return ResponseHandler.usual(False, {
                'message': str(e),
                'online': isOnline
            }, 200)


    # @protected true
    # @route /api/register-deregister
    # @methods POST
    # @params token: jwt, data: object, step: string
    # @desc used to register/deregister Telegram user
    async def registerDeregisterTelegramApp(token, data, step):  
        # steps:
        # # send_code_request
        # # register_with_code
        # # register_with_password
        # # deregister
        try:
            if data['id'] == '' or data['hash'] == '' or data['phone'] == '':
                raise ValueError(message_error_fields_empty)

            licenceDecode = UserAuthHandler.decodeLicenceJWT(token)
            if not licenceDecode:
                raise ValueError(message_token_invalidated)

            authorizedLicence = UserAuthHandler.checkLicenceIfAuthorized(token)
            if not authorizedLicence:
                raise ValueError(message_not_authorized)

            requestToHandler = await UserHandler.registerDeregisterTelegramApp(licenceDecode, data, step)
            if requestToHandler[0] == False:
                return ResponseHandler.usual(False, requestToHandler[1], 200)
            return ResponseHandler.usual(True, requestToHandler[1], 200)

        except ValueError as e:
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)

        except Exception as e:
            HelperErrorToTXT.write('user-'+UserAuthHandler.decodeLicenceJWT(request.headers['Authorization']), e, request, os.path.relpath(__file__) + ' registerDeregisterTelegramApp()')
            return ResponseHandler.usual(False, {
                'message': str(e) 
            } ,200)



    # @protected true
    # @route /api/logout
    # @methods POST
    # @params token: jwt
    # @desc used to logout from XDropPro and also deletes session file
    def telegramAndAppLogout(token):
        try:
            licenceDecode = UserAuthHandler.decodeLicenceJWT(token)
            if not licenceDecode:
                raise ValueError(message_token_invalidated)

            if os.path.exists(sessions_path + licenceDecode + '.session'):
                os.remove(sessions_path + licenceDecode + '.session')

            UserHandler.setLicenceOnlineStatus(licenceDecode, False)
            return ResponseHandler.usual(True, {
                'message': 'Session logged out successfully'
            }, 200)

        except Exception as e:
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)




    # @protected true
    # @route /api/shill
    # @methods POST
    # @params token: jwt, data: object
    # @desc used to send message to Telegram chats
    async def shill(token, data):
        try:
            if data['channel'] == '' or data['message'] == '' or data['id'] == '' or data['hash'] == '':
                raise ValueError(message_error_fields_empty)

            licenceDecode = UserAuthHandler.decodeLicenceJWT(token)
            if not licenceDecode:
                raise ValueError(message_token_invalidated)

            authorizedLicence = UserAuthHandler.checkLicenceIfAuthorized(token)
            if not authorizedLicence:
                raise ValueError(message_not_authorized)

            sendMessage = await UserHandler.shill(licenceDecode, data['id'], data['hash'], data['channel'], data['message'])            
            if sendMessage[0] == False:
                return ResponseHandler.usual(False, {
                    'message': sendMessage[1]
                }, 200)        
            else:
                return ResponseHandler.usual(True, {
                    'message': sendMessage[1]
                }, 200)
        
        except Exception as e:
            HelperErrorToTXT.write('user-'+UserAuthHandler.decodeLicenceJWT(token), e, request, os.path.relpath(__file__) + ' shill()')
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)


    # @protected true
    # @route /api/profile
    # @methods GET
    # @params none
    # @desc get profile information from DB
    def getProfileData(token):
        try:
            licenceDecode = UserAuthHandler.decodeLicenceJWT(token)
            if not licenceDecode:
                raise ValueError(message_token_invalidated)

            authorizedLicence = UserAuthHandler.checkLicenceIfAuthorized(token)
            if not authorizedLicence:
                raise ValueError(message_not_authorized)
                
            return ResponseHandler.usual(True, UserGeneralHandler.getProfileData(licenceDecode))

        except Exception as e:
            HelperErrorToTXT.write('user-' + UserAuthHandler.decodeLicenceJWT(token), e, request, os.path.relpath(__file__) + ' getProfileData()')
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)

    def getAppInfo(token):
        try:
            licenceDecode = UserAuthHandler.decodeLicenceJWT(token)
            if not licenceDecode:
                raise ValueError(message_token_invalidated)

            authorizedLicence = UserAuthHandler.checkLicenceIfAuthorized(token)
            if not authorizedLicence:
                raise ValueError(message_not_authorized)
                
            return ResponseHandler.usual(True, UserGeneralHandler.getVersion(licenceDecode))

        except Exception as e:
            HelperErrorToTXT.write('user-' + UserAuthHandler.decodeLicenceJWT(token), e, request, os.path.relpath(__file__) + ' getProfileData()')
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)



    def sessionLogout(licence):
        try:
            if os.path.exists(sessions_path + licence + '.session'):
                os.remove(sessions_path + licence + '.session')
            UserHandler.setLicenceOnlineStatus(licence, False)
            return ResponseHandler.usual(True, {
                'message': 'Session logged out successfully'
            }, 200)
        except Exception as e:
            return ResponseHandler.usual(False, {
                'message': str(e)
            }, 200)