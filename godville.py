#!/usr/bin/python
import requests
import json

username='YOURNAME'

json_data=requests.get("http://godville.net/gods/api/"+username+".json")

print(data)
