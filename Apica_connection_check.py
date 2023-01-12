import time
import sys
from snowflake.connector import connect
import logging
import json
import pandas as pd

USER = 'SVC_SNOWDEV_EDPDEV_APICA'
PASSWORD = 'sn0wflak3_SF@apicadev9'
ACCOUNT = 'deltadentalins-dev'

start = time.time()


#json = df.to_json()
#print(json)
end = time.time()

json_return = {
  'returncode': 0,
  'start_time': start,
  'value': 0,
  'end_time': end,
  'message': 'HTTP Call completed with status OK',
  'metrics': {
    'duration': 0,
    'content_size': 1256,
    'header_count': 11,
    'http_status': 200
  }
}

print(json.dumps(json_return))
cursor.close()
#print('Closed Snowflake connection')
