#!/usr/bin/env python

#from marvel_api import MarvelAPIObject
import time
import hashlib
import sys
import getopt
import os
from optparse import OptionParser, make_option
from pprint import pprint
import requests
import json
import random
import argparse
import atexit


# Marvel API keys
marvel_public_key = ''
marvel_private_key = ''

#Attribution = "Data provided by Marvel. 2014 Marvel"

##############################
def main(argv):

    # Ensure to set up Marvel API keys
    if marvel_public_key == '' or marvel_private_key == '':
        print "\nPlease configure your Marvel Public/Private API Key by setting marvel_public_key and marvel_private_key variable\n"
        return -1

    timestamp = str(int(time.time()))
    # hash is required as part of request which is md5(timestamp + private + public key)
    API_KEY = hashlib.md5(timestamp + marvel_private_key + marvel_public_key).hexdigest()

    character = "wolverine"

    # GET /v1/public/character
    url = 'http://gateway.marvel.com:80/v1/public/characters?name=' + character + '&apikey=' + marvel_public_key + '&ts=' + timestamp + '&hash=' + API_KEY
    headers = {
        'content-type':'application/json'
        }
    request = requests.get(url, headers=headers)
    data = json.loads(request.content)

    description = data['data']['results'][0]['description']
    # this is an example of a URL built from a resource URI returned
    junk = 'http://gateway.marvel.com/v1/public/comics/41112' + '?apikey=' + marvel_public_key + '&ts=' + timestamp + '&hash=' + API_KEY

    print url
    print description
    print junk
    return 0

# Start program

if __name__ == "__main__":
   main(sys.argv[1:])




