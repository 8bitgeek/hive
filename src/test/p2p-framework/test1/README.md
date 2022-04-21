# Basic outer P2P functional test.

Requires two nodes to run on localhost. Make a TCB connection with one another, send a message 'Hi There!', and then disconnect.

# Node 1:

`./test1-node1.py`

# Node 2:

`./test1-node2.py`

# Expected Output:

```

Initialisation of the Node on port: 10001 on node (b6e75a549c90d838a94cfb5c003af90b492cba7ad5d4d830d5ee12ceeb38d0c0b4991544e85ac9595080d2ddf4f5628b98ef1b532eedee72df2adb4f14afe727)

inbound_node_connected: 5a2794b197d425167d9966e7726089eae24216da15850db42acffb3295dad251dfd42a26b96f61b510415f4ebb5affaef6de89a826e1c4c3835dbc41d1bddbf4
node_message from 5a2794b197d425167d9966e7726089eae24216da15850db42acffb3295dad251dfd42a26b96f61b510415f4ebb5affaef6de89a826e1c4c3835dbc41d1bddbf4: {'message': 'Hi there!'}

```

