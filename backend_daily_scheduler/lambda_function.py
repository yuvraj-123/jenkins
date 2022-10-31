import os
import json
import logging
import urllib3

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
DEV_SITE = os.environ['dev_site']

def lambda_handler(event, context):
    try:
        http = urllib3.PoolManager()
    
        dev = http.request('GET', DEV_SITE, headers={'User-Agent': 'AWS Lambda'})
        prod = http.request('GET', SITE, headers={'User-Agent': 'AWS Lambda'})
        
        print(json.loads(dev.data.decode('utf-8')))
        print(json.loads(prod.data.decode('utf-8')))
    except Exception as e:
        message = "Failed to perform backend_hourly_scheduler. Exception: {}".format(e)
        logging.exception(message)
