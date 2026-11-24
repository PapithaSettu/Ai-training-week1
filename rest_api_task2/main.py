import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("API_KEY")
print("API_KEY from.env:",api_key)

# send x-API-key header

try:
    response=requests.get("https://httpbin.org/headers",headers={"X-API-KEY":api_key},timeout=5,)
    response.raise_for_status()
    data=response.json()

    #nested json
    received_key=data.get("headers",{}).get("X-Api-Key")
    print("Server received key:",received_key)

    #save parsed result to resultjson

    result={"received_key":received_key,"status":response.status_code}
    with open("result.json","w")as file:
        json.dump(result,file,indent=4)

except requests.exceptions.Timeout:
    print("Timeout: please try again")
except requests.exceptions.ConnectionError:
    print("Connection error: check your internet")

#timeout test:delay 10s
try:
   response= requests.get("https://httpbin.org/delay/10",timeout=3)
except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")
except requests.exceptions.ConnectionError:
    print("Connection error: check your internet")

    #http 500 handle with raise_for_status
try:
    response=requests.get("https://httpbin.org/status/500",timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("Server error 500 handled")
except requests.exceptions.Timeout:
    print("timeout:please try again")    
except requests.exceptions.ConnectionError:
    print("Connection error:check your internet")    

                       
              