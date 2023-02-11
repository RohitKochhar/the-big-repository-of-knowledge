# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: log_emitter.py
#
# 	File Description: Program to send logs to RMQ
# 
# 	File History:
# 		- 2022-06-21: Created by Rohit S.
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
    o_Rabids = RabidsMQ(s_Host='18.117.132.74')
    # Open channel
    o_Rabids.openChannel()
    # Declare the exchange
    o_Rabids.o_Channel.exchange_declare(
        exchange='logs',
        exchange_type='fanout'
    )
    # Create message
    s_Message = ' '.join(sys.argv[1:]) or "Default Log"
    # Publish to the exchange
    o_Rabids.basicPublish(
        s_Exchange      = 'logs',
        s_RoutingKey    = '',
        s_Body          = s_Message
    )
    # Close the queue
    o_Rabids.o_Channel.close()
