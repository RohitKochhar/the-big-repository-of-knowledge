# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: log_emitter.py
#
# 	File Description:   Log emitter to send messages
#                       with topics to an exchange
# 
# 	File History:
# 		- 2022-06-23: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import time, pika, sys, os
sys.path.append('../')
from RabidsMQ import RabidsMQ

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    print('Running log_emitter')
    # Define RabidsMQ instance
    o_Rabids = RabidsMQ(s_Host='localhost')
    # Open channel
    o_Rabids.openChannel()
    # Create message and severity
    s_Message = (sys.argv[1]) or "Default Log"
    s_Severity = (sys.argv[2]) or "LOW"
    # Declare the exchange
    o_Rabids.o_Channel.exchange_declare(
        exchange='direct_logs', 
        exchange_type='direct'
    )
    # Publish to the exchange
    o_Rabids.basicPublish(
        s_Exchange      = 'direct_logs',
        s_RoutingKey    = s_Severity,
        s_Body          = s_Message
    )
    # Close the queue
    o_Rabids.o_Channel.close()
