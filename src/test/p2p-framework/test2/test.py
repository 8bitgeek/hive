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
import copy

# common imports location
sys.path.append("../../../bin")

from HiveAStar import HiveAStar

#
# 0 is available path
# 1 is unavailable
# 2 is chosen path
#
grid =  [
            [0,0,1,0,1],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [1,0,1,0,0],
            [0,0,1,0,0]   
        ]

result =  [
            [2,2,1,0,1],
            [0,1,2,1,0],
            [0,1,2,1,2],
            [1,0,1,2,0],
            [0,0,1,0,0]   
        ]


# x horizontal, y vertical#
# nodeN[0] == x, nodeN[1] == y
nodeA=[0,0]    # Origin (x,y)
nodeB=[2,4]    # Destination (x,y)

astar=HiveAStar(grid)
path=astar.solve(nodeA,nodeB)

# populate the input grid with the path result
for node in path:
    y, x = node.point
    grid[y][x]=2

# compare the computed path with the composite
# result
if ( grid == result ):
    sys.exit(0)

# result comparison failed
sys.exit(255)
