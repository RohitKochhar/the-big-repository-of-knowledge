# File Information ---------------------------------------------
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# 	File Name: RabidsMQ.py
#
# 	File Description:   Contains class definition of RabidsMQ
#                       a reuseable manager class to configure 
#                       RabbitMQ clients
# 
# 	File History:
# 		- 2022-06-19: Created by Rohit S.
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# Imports --------------------------------------------------------
import pika

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------
class RabidsMQ:
    def __init__(self, s_Host='localhost') -> None:
        self.s_Host = s_Host

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    #
    #	Function Name:          openConnection
    #
    #	Function Description:   resusable function to init RabbitMQ channel
    #
    #	Function History:
    #		- 2022-06-19: Created by Rohit S.
    #
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    def openChannel(self) -> None:
        # Open Connection Channel
        o_ConnectionParameters = pika.ConnectionParameters(self.s_Host)
        o_Connection    = pika.BlockingConnection(o_ConnectionParameters)
        o_Channel       = o_Connection.channel()
        self.o_Channel  = o_Channel

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    #
    #	Function Name:          basicPublish
    #
    #	Function Description:   Sends basic message
    #
    #	Function History:
    #		- 2022-06-19: Created by Rohit S.
    #
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    def basicPublish(self, s_Exchange, s_RoutingKey, s_Body):
        self.o_Channel.basic_publish(
            exchange        = s_Exchange,
            routing_key     = s_RoutingKey,
            body            = s_Body
        )

        if s_Exchange == '':
            print(f'[------>] Sent message "{s_Body}" to queue: {s_RoutingKey}')
        else:
            print(f'[------>] Sent message "{s_Body}" to queue: {s_RoutingKey} via {s_Exchange}')

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    #
    #	Function Name:          basicConsume
    #
    #	Function Description:   consumes basic message
    #
    #	Function History:
    #		- 2022-06-19: Created by Rohit S.
    #
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    def basicConsume(self, s_Queue, F_Callback, b_AutoAck=False):        
        def callbackWrapper(ch, method, properties, body):
            print(f"[<-------] Received {body} to {s_Queue}")
            F_Callback(ch, method, properties, body)

        self.o_Channel.basic_consume(
            queue               = s_Queue,
            auto_ack            = b_AutoAck,
            on_message_callback = callbackWrapper,
        )