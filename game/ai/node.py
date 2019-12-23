# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:02:10 2019

@author: simslay
"""

class Node():
    state = None
    action = None
    parent = None
    depth = None
    f = None
    expanded = None

    def __init__(self, state, move, f, depth):
        self.state = state
        self.action = move
        self.parent = None
        self.depth = depth
        self.f = f
        self.expanded = True