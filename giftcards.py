# Author: Christopher Haley
#ADD in API KEY
import requests
import json
#can only create one card currently don't know why
def createCard(*args,**kwargs):
    try:
        headers = {
            "Authorization":"api-key" +"API KEY",
            "type":"MERCHANT_LOCKED",
            "hostname": kwargs['hostname']
            }
    except:
        headers = {
            "Authorization":"api-key +"API KEY",
            "type":"MERCHANT_LOCKED"
            }
        
    requests.post("https://sandbox.privacy.com/v1/card",headers = headers)
    

def getCards(*args,**kwargs):
    headers = {
        "Authorization":"api-key +"API KEY",
    }
    response = requests.get("https://sandbox.privacy.com/v1/card?page=2",headers = headers).json()
    return response
createCard()
print(getCards())