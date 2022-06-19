# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: consumer.py
#
# 	File Description:   Contains consumers to read messages from
#                       RabbitMQ task queue
# 
# 	File History:
# 		- 2022-06-19: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import time, pika, sys, os
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
#		- 2022-06-19: Created by Rohit S.
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
def main():
    s_Host      = "localhost"
    o_Channel   = openChannel(s_Host)
    # Declare queue
    o_Channel.queue_declare(queue='task_queue', durable=True)
    # Attach callback
    o_Channel.basic_consume(
        queue                   = 'task_queue',
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
#		- 2022-06-19: Created by Rohit S.
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
def callback(ch, method, properties, body):
    print(f"[<----] Received {str(body)}")
    time.sleep(body.count(b'.'))
    print("[X] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

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
    o_Channel.basic_qos(prefetch_count=1)
    return o_Channel

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