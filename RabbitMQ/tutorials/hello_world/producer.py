# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: producer.py
#
# 	File Description: Contains RabbitMQ producer
# 
# 	File History:
# 		- 2022-06-18: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
# Need sys to import RabidsMQ
import sys
sys.path.append('../')
from RabidsMQ import RabidsMQ 

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    # Open Connection Channel
    o_RabidsMQ      = RabidsMQ(s_Host='localhost')
    o_RabidsMQ.openChannel()
    o_RabidsMQ.o_Channel.queue_declare(queue='hello')
    o_RabidsMQ.basicPublish(
        s_Exchange      = "",
        s_RoutingKey    = "hello",
        s_Body          = "Hello, World!"
    )
    o_RabidsMQ.o_Channel.close()