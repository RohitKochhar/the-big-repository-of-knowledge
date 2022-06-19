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
import pika

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    # Open Connection Channel
    o_ConnectionParameters = pika.ConnectionParameters('localhost')
    o_Connection    = pika.BlockingConnection(o_ConnectionParameters)
    o_Channel       = o_Connection.channel()
    # Declare message queue "hello"
    o_Channel.queue_declare(queue='hello')
    # Send the message
    o_Channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!'
    )
    # Indicate that we sent the message
    print("[---->] Sent message 'Hello World!'")
    # Close the connection
    o_Connection.close()