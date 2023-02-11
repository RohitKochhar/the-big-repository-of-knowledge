# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: consumer.py
#
# 	File Description: Contains RabbitMQ consumer
# 
# 	File History:
# 		- 2022-06-18: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import sys, os
sys.path.append('../')
from RabidsMQ import RabidsMQ

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#
#	Function Name: main()
#
#	Function Description: Creates communication channel and 
#                         attaches callback to queue.
#
#	Function Inputs: None
#
#	Function Outputs: None
#
#	Function History:
#		- 2022-06-18: Created by Rohit S.
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
def main():
    # Create RabidsMQ instance
    o_RabidsMQ      = RabidsMQ(s_Host='18.118.129.94')
    # Open connection
    o_RabidsMQ.openChannel()
    # Declare queue
    o_RabidsMQ.o_Channel.queue_declare('hello')
    # Define consumption
    o_RabidsMQ.basicConsume(
        s_Queue         = 'hello',
        F_Callback      = lambda ch, method, properties, body: None,
        b_AutoAck       = True
    )

    print("Waiting for messages...")
    # Start consuming
    o_RabidsMQ.o_Channel.start_consuming()



# Main Call ------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)