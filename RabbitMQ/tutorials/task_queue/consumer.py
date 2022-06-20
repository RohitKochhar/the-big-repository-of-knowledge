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
sys.path.append('../')
from RabidsMQ import RabidsMQ

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------
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
def callback(ch, method, properties, data):
    body = data["s_Body"]
    t_StartTime = time.time()
    time.sleep(body.count('.'))
    t_EndTime   = time.time()
    print(f"[COMPLETED]\n\tTask: {body.split('.')[0]}\n\tCompletion Time: {round(t_EndTime-t_StartTime, 3)}\n")
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    try:
        # Create RabidsMQ instance
        o_RabidsMQ      = RabidsMQ(s_Host='localhost')
        o_RabidsMQ.openChannel()
        o_RabidsMQ.o_Channel.queue_declare(queue='task_queue', durable=True)
        o_RabidsMQ.o_Channel.basic_qos(prefetch_count=1)
        o_RabidsMQ.basicConsume(
            s_Queue     = 'task_queue',
            F_Callback  = callback
        )
        # Set QoS
        print("Waiting for messages...")
        # Start consuming
        o_RabidsMQ.o_Channel.start_consuming()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)