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
import sys
import time

# common imports location
sys.path.append("../../../bin")

from AStar import AStar

#
# '.' is available
# '%' is unavailable
#
grid = []
grid.append(list('..%.%'))
grid.append(list('.%.%.'))
grid.append(list('.%.%.'))
grid.append(list('%.%..'))
grid.append(list('..%..'))

astart=AStar(grid)

inputA='0 0'    # Origin (x,y)
inputB='3 3'    # Destination (x,y)

nodeA_x, nodeA_y = [ int(i) for i in inputA.split() ]
nodeB_x, nodeB_y = [ int(i) for i in inputB.split() ]

path=astart.solve((nodeA_x, nodeA_y),(nodeB_x, nodeB_y))

# dump the path list coords
print(len(path) - 1)
for node in path:
    x, y = node.point
    print(x, y)
