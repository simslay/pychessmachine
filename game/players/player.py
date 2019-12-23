# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:18:30 2019

@author: simslay
"""
from abc import abstractmethod
import enum

class Fevals(enum.Enum):
    w_feval = 1
    b_feval = 2
    w_alea = 3
    b_alea = 4
    w_captures = 5
    b_captures = 6
    w_stalemate = 7
    b_stalemate = 8
    w_checkmate = 9
    b_checkmate = 10

class Player():
    alliance = None
    ptype = None
    feval = None
    
    def __init__(self):
        pass
    
    @abstractmethod
    def enter_move(self, game, check):
        pass
    
    