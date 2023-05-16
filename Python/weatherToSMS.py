'''
Jodi
This script pulls weather info from National weather api, and sends SMS with todays forecast
'''

from twilio.rest import Client
import requests
import json
import os
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    #setting the header tells the computer how to interpret the data
    headers = {'USer-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

    #sensitive variables stored as Environment Variable for securtiy
    url = os.environ['URL']
    weatherPull = requests.get(url, headers=headers, timeout=2)

    #numbers = []
    #parse json variables
    json_data = json.loads(weatherPull.text)

    tempData = json_data['properties']
    weekDict = {}

    #runs through weekdays, and checks for data associated with Day time. If found, that data isstored in a seperate dictionary
    for v in tempData['periods']:
        if bool(v['isDaytime']):
            weekDay = v['name'] + " " + str(v['temperature'])+v['temperatureUnit']
            dayForecast = v['detailedForecast']
            weekDict.update({weekDay:dayForecast})

    #pulls 1st entry of Dictionary
    msg = {k: weekDict[k] for k in list(weekDict)[:1]}
    cleanMsg = str(msg)[1:-1]# + " " + str(msg)[16:-2])
    message = cleanMsg

    #Sets up text to send. Sensitive data stored as Env variables
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    from_phone = os.environ['FROM_PHONE']
    to_phone = os.environ['TO_PHONE']
    to_phone2 = os.environ['TO_PHONE2']
    phoneNumbers = [to_phone, to_phone2]

    # sends message to all numbers in phoneNumbers array
    for num in phoneNumbers:
        client.messages.create(body=message,from_=from_phone,to=num)




