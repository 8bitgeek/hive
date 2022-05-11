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

class AStarNode:
    
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    
    def move_cost(self,other):
        return 0 if self.value == '.' else 1


class HiveAStar:
    def __init__(self,grid):
        self.grid = grid
        self.path = []

    # default is simple manhattan line heuristic.
    # overload with a network derived heuristic value.
    def heuristic(self,point1,point2):
        return abs(point1.point[0] - point2.point[0]) + abs(point1.point[1]-point2.point[0])
    
    def children(self,point):
        x,y = point.point
        links=[]
        for x_offs in range(-1,2):
            x_link=(x+x_offs)
            if x_link>=0:
                for y_offs in range(-1,2):
                    y_link=y+y_offs
                    if y_link>=0:
                        link = self.grid[x_link][y_link]
                        if link.value == 0:
                            links.append(link)
        return links
    
    def search(self,start, goal):
        openset = set()
        closedset = set()
        current = start
        openset.add(current)
        # While not empty set...
        while openset:
            # Find the item in the open set with the lowest G + H score
            current = min(openset, key=lambda o:o.G + o.H)
            # At goal? Walk the path back
            # and return the path from start to goal
            if current == goal:
                self.path = []
                while current.parent:
                    self.path.append(current)
                    current = current.parent
                self.path.append(current)
                return self.path[::-1]
            # Transfer item from open to closed set.
            openset.remove(current)
            closedset.add(current)
            # Itterate adjasent nodes...
            for node in self.children(current):
                # In closed set? skip it...
                if node in closedset:
                    continue
                # In open set? ...
                if node in openset:
                    # Is current G score better that closed node? 
                    new_g = current.G + current.move_cost(node)
                    if node.G > new_g:
                        # Yes, re-parent the node.
                        node.G = new_g
                        node.parent = current
                else:
                    # If it isn't in the open set, 
                    # calculate the G and H to score for the node
                    node.G = current.G + current.move_cost(node)
                    node.H = self.heuristic(node, goal)
                    # Set the parent as our current item
                    node.parent = current
                    # Append it to the set
                    openset.add(node)
        # No Route
        # Return an empty set
        return []

    def solve(self,nodeA,nodeB):
        # Convert all the points to instances of HiveAStar
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                self.grid[x][y] = AStarNode(self.grid[x][y],(x,y))
        # Get the path
        self.path=self.search(self.grid[nodeA[0]][nodeA[1]],self.grid[nodeB[0]][nodeB[1]])
        return self.path

