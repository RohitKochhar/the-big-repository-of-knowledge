# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: log_consumer.py
#
# 	File Description: 
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
    print('Running log_consumer')
    try:
        # Define Rabids MQ instance
        o_Rabids = RabidsMQ(s_Host='18.117.132.74')
        # Open channel 
        o_Rabids.openChannel()
        # Declare exchange
        o_Rabids.o_Channel.exchange_declare(exchange='logs', exchange_type='fanout')
        # Store the resulting queue name
        s_QueueName = o_Rabids.o_Channel.queue_declare(queue='', exclusive=True).method.queue
        # Bind the channel's queue to the exchange
        o_Rabids.o_Channel.queue_bind(exchange='logs', queue=s_QueueName)
        # Wait for logs
        print("Waiting for logs...")
        o_Rabids.basicConsume(
            s_Queue=s_QueueName,
            F_Callback= (lambda ch, method, properties, body: body),
            b_AutoAck=True
        )
        # Start consuming
        o_Rabids.o_Channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)