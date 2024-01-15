
class ResponseHandler():
    
    def error_success_handler(message, error_alert, success_alert, error_type):
        return {
            "message": message,
            "error_alert_on": error_alert,
            "success_alert_on": success_alert,
            "error_type": error_type
        }

    def responseHandler(data_type, data):
        return {
            "data_type": data_type,
            "data": data
        }

    def usual(success, data={}, code=200):
        return {
            "success": success,
            "data": data
        }, code