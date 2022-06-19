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
import pika, sys, os

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
    # Create connection
    o_ConnectionParamers = pika.ConnectionParameters('localhost')
    o_Connection = pika.BlockingConnection(o_ConnectionParamers)
    o_Channel = o_Connection.channel()
    # Declare the queue again
    o_Channel.queue_declare('hello')
    # Attach callback
    o_Channel.basic_consume(
        queue                   = 'hello',
        auto_ack                = True,
        on_message_callback     = callback
    )
    print("Waiting for messages...")
    # Start consuming
    o_Channel.start_consuming()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#
#	Function Name: callback
#
#	Function Description: Lets queue what to know when a message
#                           comes in
#
#	Function Inputs:
#           - ch:           BlockingChannel item used to create connection
#           - method:       Item declaring how message was sent
#           - properties:   Item containing properties of message
#           - body:         Binary string containing sent message
#
#	Function Outputs:
#
#	Function History:
#		- 2022-06-18: Created by Rohit S.
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
def callback(ch, method, properties, body):
    print(f"[<----] Received {str(body)} at {properties}")

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