from flask import Flask, jsonify, abort, make_response, request, url_for, g, render_template
from pprint import pprint
import requests, os, urllib,cStringIO
url = 'https://api.venmo.com/v1/oauth/authorize?client_id=3363&scope=make_payments%20access_profile&response_type=token'
r = requests.request(url)
print(r)




url = 'https://api.venmo.com/v1/payments?access_token=4f79c974de90e444de8dfa56904fd0b73e8b261950f1f0d759082f59a4ce80c2'
r = requests.get(url)
response = r.json()
print(response)
#length = len(response['data'])
#print(length)
#for number in range(0, length):
#	pprint(response['data'][number]['amount'])
