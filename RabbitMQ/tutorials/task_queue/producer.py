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
sys.path.append('../')
from RabidsMQ import RabidsMQ

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------

# Function Declarations ------------------------------------------

# Main Call ------------------------------------------------------
if __name__ == '__main__':
    # Read commandline for message
    s_Message = ' '.join(sys.argv[1:]) or "Default Message"
    # Create RabidsMQ instance
    o_RabidsMQ  = RabidsMQ(s_Host='18.117.132.74')
    o_RabidsMQ.openChannel()
    o_RabidsMQ.o_Channel.queue_declare(queue='task_queue', durable=True)
    # Send the message
    o_RabidsMQ.basicPublish(
        s_Exchange='',
        s_RoutingKey="task_queue",
        s_Body=s_Message,
        properties=pika.BasicProperties(
            delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    o_RabidsMQ.o_Channel.close()