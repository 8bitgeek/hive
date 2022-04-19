#!/usr/bin/python3
# ______  ______             
# ___  / / /__(_)__   ______ 
# __  /_/ /__  /__ | / /  _ \
# _  __  / _  / __ |/ //  __/
# /_/ /_/  /_/  _____/ \___/ 
#
from p2pnetwork.node import Node
from p2pnetwork.nodeconnection import NodeConnection

# NodeConnection class only hold the TCP/IP connection with the other node, 
# to manage the different connections to and from the main node. It does 
# not implement application specific elements. Mostly, you will only need 
# to extend the Node class. However, when you would like to create your 
# own NodeConnection class you can do this. Make sure that you override 
# create_new_connection(self, connection, id, host, port) in the class 
# Node, to make sure you initiate your own NodeConnection class
class OuterNodeConnection (NodeConnection):
    # Python class constructor
     def __init__(self, main_node, sock, id, host, port):
        super(OuterNodeConnection, self).__init__(main_node, sock, id, host, port)

    # Check yourself what you would like to change and override! See the 
    # documentation and code of the nodeconnection class.

class OuterPeer2PeerNode (Node):
    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(OuterPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)
        
    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + str(data))
        
    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop!")

    # OPTIONAL
    # If you need to override the NodeConection as well, you need to
    # override this method! In this method, you can initiate
    # you own NodeConnection class.
    def create_new_connection(self, connection, id, host, port):
        return OuterNodeConnection(self, connection, id, host, port)
