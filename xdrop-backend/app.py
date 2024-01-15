# pip install flask[async]
# pip install flask_cors
# pip install pymongo
# pip install telethon
# pip install pyjwt
# pip install waitress
# pip install python-dotenv

from flask import Flask, request
from flask_cors import CORS
from handlers.env import EnvironmentHandler

main_host = '0.0.0.0'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretonmyass2'
CORS(app, supports_credentials=True, expose_headers="Authorization")



##################################
####    ADMIN ROUTES #############
##################################
from controllers.admin import AdminController


@app.route('/xdropadmin/login/admin-login', methods=['POST'])
def adminLogin():
    return AdminController.login(request.json)

@app.route('/xdropadmin/admin/get/licences')
def getLicences():
    token = request.headers['Authorization']
    return AdminController.getAllLicences(token)

@app.route('/xdropadmin/get-all/licences/number')
def getLicencesNumber():
    token = request.headers['Authorization']
    return AdminController.getLicencesNumber(token)

@app.route('/xdropadmin/admin/update/length/licence', methods=['POST'])
def extendLicence():
    token = request.headers['Authorization']
    data = request.json
    return AdminController.extendLicence(token, data)

@app.route('/xdropadmin/admin/admin-create/new-licence', methods=['POST'])
def createLicence():
    token = request.headers['Authorization']
    data = request.json
    return AdminController.createLicence(token, data)

@app.route('/xdropadmin/admin/get-all/default/messages')
def getDefaultMessages():
    token = request.headers['Authorization']
    return AdminController.getDefaultMessages(token)

@app.route('/xdropadmin/admin/set-all/default-messages', methods=['POST'])
def setDefaultMessages():
    token = request.headers['Authorization']
    data = request.json
    return AdminController.setDefaultMessages(token, data)







##################################
####    USER ROUTES ##############
##################################
from controllers.user import UserController

# LOGIN USING LICENCE
@app.route('/api/login', methods=['POST'])
def login():
    licence = request.json['licence']
    return UserController.login(licence)


# REGISTER TELEGRAM APP
@app.route('/api/register-deregister', methods=['POST'])
async def registeringAndDeregistering():
    step = request.args.get('step')
    token = request.headers['Authorization']
    data = request.json    
    return await UserController.registerDeregisterTelegramApp(token, data, step)
       
# MAIN APP AND TELEGRAM APP LOGOUT ROUTE
@app.route('/api/logout', methods=['POST'])
def appLogout():
    token = request.headers['Authorization']
    return UserController.telegramAndAppLogout(token)


# MAIN SHILLING ROUTE
@app.route('/api/shill', methods=['POST'])
async def shill():
    token = request.headers['Authorization']
    data = request.json
    return await UserController.shill(token, data)

@app.route('/api/sessionLogout', methods=['POST'])
def deleteSession():
    licence = request.json['licence']
    return UserController.sessionLogout(licence)

# GET LICENCE AND ITS VALIDITY
@app.route('/api/profile')
def getProfile():
    token = request.headers['Authorization']
    return UserController.getProfileData(token)

# GET APP INFO
@app.route('/api/app', methods=['GET'])
def getAppInfo():
    token = request.headers['Authorization']
    return UserController.getAppInfo(token)
        
    
    

# # API TEST ROUTE  # #
@app.route('/test')
def test():
    return '<h1 style="text-align: center;">hello world!</h1>'


# if __name__ == '__main__':
#     from waitress import serve
#     serve(app, host=main_host, port=envs['port'])

if __name__ == '__main__':
    app.run(host=main_host, port=EnvironmentHandler.getEnvs()['port'], debug=True, threaded=True)