import json
from urllib import request
import requests

API_request=requests.get("https://hourlypricing.comed.com/api?type=currenthouraverage")
prices_data=API_request.text
parse_json=json.loads(prices_data)
prices=parse_json[0]['price']