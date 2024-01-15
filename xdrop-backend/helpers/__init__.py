from datetime import datetime
import random, string

class HelperErrorToTXT():

    def write(userType, exception, request, function):
        f = None
        now = datetime.now()
        if userType == 'admin':
            f = open('request_error_log/admin.txt', 'a')
        else:
            f = open('request_error_log/'+userType+'.txt', 'a')

        f.write('# '+function+' --- '+now.strftime('%d/%m/%Y, %H:%M:%S') +'--- EXCEPTION: '+ str(exception) +' --- REQUEST: '+ str(request)+' #\n')
        f.close()




class GenerateRandomStringAgainstDB():

    def arrayContainsItem(item, array):
        for arrItem in array:
            if item == arrItem:
                return True
        return False

    def generateRandomUniqueStrings(length, comparison):
        generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
        check = GenerateRandomStringAgainstDB.arrayContainsItem(generatedString, comparison)
        while check == True:
            generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
            check = GenerateRandomStringAgainstDB.arrayContainsItem(generatedString, comparison)

        return generatedString