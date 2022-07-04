# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: simpleWrite.py
#
# 	File Description: 
#       - Outlines simple write operations to influx DB
#       - Simulates a 1 Hz temperature reading 
#
# 	File History:
# 		- 2022-07-01: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from random import randint
from time import sleep

# Global Variables -----------------------------------------------
BUCKET      = "test_bucket"            
ORG         = "test_org"
TOKEN       = "k-7ktWnQuBJ_4R2W7YZA-uoaMo6242opAaqQ5_60W_PRBPEJZQ0rcYeQnIFuLfMoyRskFQ9Qqy4UyENP673EUA=="
URL         = "http://localhost:8086"

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    print('Running simpleReadWrite')
    o_Client = influxdb_client.InfluxDBClient(
        url     = URL, 
        token   = TOKEN,
        org     = ORG,
    )

    while True:
        # Create the client instance
        o_WriteAPI = o_Client.write_api(write_options=SYNCHRONOUS)
        # Create a random temperature reading
        i_RandTemp = 20 + (randint(-10,10) / 10)
        # Point the random temperature to waterloo location weather collection
        p = influxdb_client.Point("weather").tag("location", "Waterloo").field("temperature", i_RandTemp)
        # Write the point to the bucket
        o_WriteAPI.write(bucket=BUCKET, org=ORG, record=p)
        # Wait a second before continuing
        sleep(1)
