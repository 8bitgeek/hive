#!/usr/bin/python3
# ______  ______             
# ___  / / /__(_)__   ______ 
# __  /_/ /__  /__ | / /  _ \
# _  __  / _  / __ |/ //  __/
# /_/ /_/  /_/  _____/ \___/ 
#
# The MIT License (MIT)
#
# Copyright © 2022 8bitgeek at github
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the “Software”), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
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
class HiveOuterNodeConnection (NodeConnection):
    # Python class constructor
     def __init__(self, main_node, sock, id, host, port):
        super(HiveOuterNodeConnection, self).__init__(main_node, sock, id, host, port)

    # Check yourself what you would like to change and override! See the 
    # documentation and code of the nodeconnection class.

class HiveOuterNode (Node):
    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(HiveOuterNode, self).__init__(host, port, id, callback, max_connections)

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
        return HiveOuterNodeConnection(self, connection, id, host, port)
