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
import pika, json, time

# Global Variables -----------------------------------------------

# Class Declarations ---------------------------------------------
class RabidsMQ:
    def __init__(self, s_Host='localhost') -> None:
        self.i_ReceivedCount    = 0    
        self.s_Host             = s_Host

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
    def basicPublish(self, s_Exchange, s_RoutingKey, s_Body, properties=pika.BasicProperties()):
        self.o_Channel.basic_publish(
            exchange        = s_Exchange,
            routing_key     = s_RoutingKey,
            body            = self.packData(s_Body, s_RoutingKey)
        )

        if s_Exchange == '':
            print(f'[SENT >>>] Sent message "{s_Body}" with routing key: {s_RoutingKey}')
        else:
            print(f'[SENT >>>] Sent message "{s_Body}" with routing key: {s_RoutingKey} via {s_Exchange}')

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
            d_Packet = self.unpackData(body)
            print(f"[>>> GOT]\n\tBody: {d_Packet['s_Body']}\n\tQueue: {d_Packet['s_Queue']}\n\tResolution Time: {round(time.time() - int(d_Packet['t_Sent']), 3)} seconds\n\tReceived Packets at this worker: {self.i_ReceivedCount}")
            F_Callback(ch, method, properties, d_Packet)
            self.i_ReceivedCount += 1

        self.o_Channel.basic_consume(
            queue               = s_Queue,
            auto_ack            = b_AutoAck,
            on_message_callback = callbackWrapper,
        )

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    #
    #	Function Name:          packData
    #
    #	Function Description:   Takes a payload and converts to JSON
    #                           with some metadata, flattens to string
    #
    #	Function History:
    #		- 2022-06-19: Created by Rohit S.
    #
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    def packData(self, s_Body, s_RoutingKey):
        d_Packet = {
            "s_Body":       s_Body,
            "s_Queue":      s_RoutingKey,
            "t_Sent":       time.time(),
        }

        return json.dumps(d_Packet)

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    #
    #	Function Name:          unpackData
    #
    #	Function Description:   Reverses the string from packData
    #
    #	Function History:
    #		- 2022-06-19: Created by Rohit S.
    #
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    def unpackData(self, s_JsonObject):
        return json.loads(s_JsonObject.decode('UTF-8'))