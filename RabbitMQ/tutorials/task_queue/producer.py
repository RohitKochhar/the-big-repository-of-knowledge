# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: producer.py
#
# 	File Description:   Contains RabbitMQ producer sending messages
#                       from commandline to a task queue
# 
# 	File History:
# 		- 2022-06-19: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import sys, pika

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#
#	Function Name:  openChannel
#
#	Function Description: resusable function to init RabbitMQ channel
#
#	Function Inputs:
#       - s_Host: Host name / IP to connect to (default = localhost)
#
#	Function Outputs:
#       - o_Channel:    Channel object created from blocking connection to
#                       host specified by s_Host
#
#	Function History:
#		- 2022-06-19: Created by Rohit S.
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
def openChannel(s_Host='localhost'):
    # Open Connection Channel
    o_ConnectionParameters = pika.ConnectionParameters(s_Host)
    o_Connection    = pika.BlockingConnection(o_ConnectionParameters)
    o_Channel       = o_Connection.channel()
    return o_Channel

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    # Read commandline for message
    s_Message = ' '.join(sys.argv[1:]) or "Default Message"
    # Open communication channel
    s_Host = 'localhost'
    o_Channel = openChannel(s_Host)
    # Declare message queue
    o_Channel.queue_declare(queue='task_queue', durable=True)
    # Send the message
    o_Channel.basic_publish(exchange='',
        routing_key="task_queue",
        body=s_Message,
        properties=pika.BasicProperties(
            delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    print(f"[-------> Sent {s_Message} to task_queue]")