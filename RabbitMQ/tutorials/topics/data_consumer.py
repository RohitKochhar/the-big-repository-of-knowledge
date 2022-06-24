# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: data_consumer.py
#
# 	File Description: Consumes topic filtered data
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
    print('Running data_consumer')
    try:
        # Define Rabids MQ instance
        o_Rabids = RabidsMQ(s_Host='localhost')
        # Open channel 
        o_Rabids.openChannel()
        # Declare exchange
        o_Rabids.o_Channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        # Store the resulting queue name
        s_QueueName = o_Rabids.o_Channel.queue_declare(queue='', exclusive=True).method.queue
        # Bind the channel's queue to the exchange depending on severites
        a_Topics = sys.argv[1:]
        for s_Topic in a_Topics:
            o_Rabids.o_Channel.queue_bind(exchange='topic_logs', queue=s_QueueName, routing_key=s_Topic)
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