#!/usr/bin/env python

import requests
import json
import argparse

# Setup the command line args
parser = argparse.ArgumentParser(description='Test Python JSON GET Script')
parser.add_argument("-l", "--uri", dest="uri", action="append", help="URI to Resource")
parser.add_argument("-u", "--user", dest="user", action="append", help="Username")
parser.add_argument("-p", "--password", dest="pwd", action="append", help="Password")
parser.add_argument("-c", "--parms", dest="parms", action="append", help="URL parameters")
args = parser.parse_args()

if args.uri:
    json_uri = args.uri
if args.user:
    json_user = args.user
if args.pwd:
    json_pwd = args.pwd
if args.parms:
    json_uri += (args.parms[0])
print (json_uri)
#Make the json request (GET)
r = requests.get(json_uri, auth=(json_user, json_pwd))
# Print the results of the JSON request
print ("-- Status code --")
print (r.status_code)
print ("-- Content type --")
print (r.headers['content-type'])
print ("-- Content Headers --")
print (r.headers)
try:
    print ("-- Reference Info --")
    print (r.json())
except:
    print ('Cound not find attribute.')
    exit(1)
