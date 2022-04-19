#!/usr/bin/python3
# ______  ______             
# ___  / / /__(_)__   ______ 
# __  /_/ /__  /__ | / /  _ \
# _  __  / _  / __ |/ //  __/
# /_/ /_/  /_/  _____/ \___/ 
#
import sys
import time

# common imports location
sys.path.append("../../../bin")

from OuterPeer2PeerNode import OuterPeer2PeerNode

node = OuterPeer2PeerNode("127.0.0.1", 10001)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10002)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()
