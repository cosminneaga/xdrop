from handlers.db import DBHandler
from telethon import TelegramClient, errors
from handlers.env import EnvironmentHandler
from handlers.auth import UserAuthHandler


# db setup
# db = DBHandler.getDBClient()
colLicences = DBHandler.getDBCollection('licences')
colMessages = DBHandler.getDBCollection('default_messages')
sessionsPath = EnvironmentHandler.getSessionPath()

class UserHandler():

    # converts licence in a JWT token and returns it to client
    def login(licence):
        return UserAuthHandler.setLicenceSessionKey(licence)

    # register/deregister telegram user
    async def registerDeregisterTelegramApp(licence, data, step):
        # steps:
        # # send_code_request
        # # register_with_code
        # # register_with_password
        # # deregister
        try:
            client = TelegramClient(sessionsPath + licence, data['id'], data['hash'])
            await client.connect()

            if step == 'send_code_request':
                code_request = await client.send_code_request(data['phone'])
                await client.disconnect()
                return (True, {
                    'id': data['id'],
                    'hash': data['hash'],
                    'phone': data['phone'],
                    'phone_code_hash': str(code_request.phone_code_hash)
                })

            elif step == 'register_with_code':
                await client.sign_in(
                    phone=data['phone'], code=data['phone_code'],
                    phone_code_hash=data['phone_code_hash']
                )
                await client.disconnect()
                return (True, {'message': 'App successfully registered.'})

            elif step == 'register_with_password':
                await client.sign_in(password=data['password'])
                await client.disconnect()
                return (True, {'message': 'App successfully registered.'})

            elif step == 'deregister':
                await client.log_out()
                return (True, {'message': 'App has been successfully deregistered.'})

        except errors.SessionPasswordNeededError:
            return (False, {
                'passwordNeeded': True
            })

        except Exception as e:
            await client.log_out()
            return (False, {
                'message': str(e)
            })


    async def shill(licenceStr, id, hash, channel, message):
        regularMessage = freeMessage = ''
        licencePlan = 'paid'
        # get default messages from db
        defaultMessagesList = list(colMessages.find({}, {'_id': 0}))
        
        if defaultMessagesList:
            regularMessage = defaultMessagesList[0]['regular']
            freeMessage = defaultMessagesList[0]['free']
        # get licence plan from db
        licence = colLicences.find_one({'key': licenceStr})
        if licence:
            licencePlan = licence['plan']

        # set extra message depending on licence plan
        if licencePlan == 'regular':
            message = message + '\n' + regularMessage
        elif licencePlan == 'free':
            message = message + '\n' + freeMessage

        # work with TelegramClient
        async with TelegramClient(sessionsPath + licenceStr, id, hash) as client:
            try:
                # start client
                await client.start()

                # send message
                await client.send_message('@'+channel, message, link_preview=True)

                # disconnect client
                await client.disconnect()

                return (True, {
                    'channel': channel
                }) 

            except errors.rpcerrorlist.SlowModeWaitError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'SlowModeWaitError for '+str(e.seconds)+' seconds',
                    'error': str(e.message),
                    'type': 'slowmode'
                })
            except errors.rpcerrorlist.ChannelPrivateError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'ChannelPrivateError',
                    'error': str(e.message),
                    'type': 'privacy'
                })
            except errors.rpcerrorlist.ChatWriteForbiddenError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'ChatWriteForbiddenError',
                    'error': str(e.message),
                    'type': 'forbidden'
                })
            except errors.rpcerrorlist.ChatRestrictedError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'ChatRestrictedError',
                    'error': str(e.message),
                    'type': 'restricted'
                })
            except errors.rpcerrorlist.UserBannedInChannelError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'UserBannedInChannelError',
                    'error': str(e.message),
                    'type': 'banned'
                })
            except errors.rpcerrorlist.TimeoutError as e:
                return (False, {
                    'channel': channel,
                    'reason': 'TimeoutError',
                    'error': str(e),
                    'type': 'timeout'
                })
            except Exception as e:
                return (False, {
                    'channel': channel,
                    'reason': 'Recommendation: restart shilling without this channel',
                    'error': str(e),
                    'type': 'general'
                })

    def setLicenceOnlineStatus(licence, status):
        colLicences.update_one({
            'key': licence
        }, {
            '$set': {
                'online': status
            }
        })