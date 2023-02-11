# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: getDriverNumberByID.py
#
# 	File Description: 
#       -   Simple toy example using HelloWorld
#       -   Uses a graphene query class to fetch driverNumber
#           from their ID
# 
# 	File History:
# 		- 2022-07-12: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
from sys import argv
from graphene import ObjectType, String, Schema

# Global Variables -----------------------------------------------
DRIVER_NUMBERS = {
    "HAM": 44,
    "RUS": 64,
    "VER": 1,
    "PER": 11,
    "LEC": 16,
    "SAI": 55,
    "NOR": 4,
    "RIC": 3,
    "ALO": 14,
    "OCO": 31,
    "GAS": 10,
    "TSU": 22,
    "BOT": 77,
    "ZHO": 24,
    "ALB": 23,
    "LAT": 6,
    "VET": 5,
    "STR": 18,
    "MAG": 20,
    "MSC": 47
}

# Class Declarations ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#	Class Name:     Query
#
#	Class Description: 
#       -   Object used to define GraphQL query
# 
#	Class History: 
# 		- 2022-07-12: Created by Rohit S.
# 
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
class Query(ObjectType):
    # Create a driver info instance
    getDriverNumber      = String(driverID=String(default_value="HAM"))

    def resolve_getDriverNumber(root, info, driverID):
        return DRIVER_NUMBERS[driverID]

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    print('Running getDriverNumberByID')
    schema = Schema(query=Query)
    try:
        driverID = argv[1]
        try:
            DRIVER_NUMBERS[driverID]
        except:
            print(f"Invalid driverID provided ({driverID}), using HAM instead")
            driverID = "HAM"
    except:
        print(f"No driverID provided, using HAM instead")
        driverID = "HAM"

    query_string = '{ getDriverNumber(driverID: "' + driverID + '") }'

    result = schema.execute(query_string)
    
    print(f"{driverID}'s number is {result.data['getDriverNumber']}")