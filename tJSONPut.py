#!/usr/bin/env python

import requests
import json
import argparse

# Setup the command line args
parser = argparse.ArgumentParser(description='Test Python JSON PUT Script')
parser.add_argument("-l", "--uri", dest="uri", action="append", help="URI to Resource")
parser.add_argument("-d", "--data", dest="data", action="append", help="JSON Data to Pass")
parser.add_argument("-u", "--user", dest="user", action="append", help="Username")
parser.add_argument("-p", "--password", dest="pwd", action="append", help="Password")
args = parser.parse_args()

if args.uri:
    json_uri = args.uri
if args.data:
    json_data = args.data
if args.user:
    json_user = args.user
if args.pwd:
    json_pwd = args.pwd
#Make the json request (PUT)
in_data = json.dumps(json_data)
json_headers = {"Content-Type": "application/json"}
print ("-- Request Data --")
print in_data
print json_headers
r = requests.put(flexeye_url, data=in_data, headers=json_headers, auth=(json_user, json_pwd))
# Print the results of the JSON request
print ("-- Status code --")
print (r.status_code)
print ("-- Content type --")
print (r.headers['content-type'])
print ("-- Content Headers --")
print (r.headers)
try:
    print ("-- Response Info --")
    print (r.json())
except:
    print ('Cound not find attribute.')
    exit(1)
