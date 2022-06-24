# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: data_emitter.py
#
# 	File Description: Sends data to topic exchange
# 
# 	File History:
# 		- 2022-06-24: Created by Rohit S.
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
    print('Running data_emitter')
    # Define RabidsMQ instance
    o_Rabids = RabidsMQ(s_Host='localhost')
    # Open channel
    o_Rabids.openChannel()
    # Create message and severity
    s_Message   = (sys.argv[1]) or "Empty Data"
    s_Topic     = (sys.argv[2]) or "anonymous.data"
    # Declare the exchange
    o_Rabids.o_Channel.exchange_declare(
        exchange='topic_logs', 
        exchange_type='topic'
    )
    # Publish to the exchange
    o_Rabids.basicPublish(
        s_Exchange      = 'topic_logs',
        s_RoutingKey    = s_Topic,
        s_Body          = s_Message
    )
    # Close the queue
    o_Rabids.o_Channel.close()
