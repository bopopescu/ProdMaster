'''
Created on 2014.03.05.

@author: fekete
'''

from tkinter import Frame
from builtins import NotImplemented

from hu.minux.prodmaster.tools.World import World

class AbstractFrame(Frame):

    _instance = None
    _myType = 'Not Implemented'


    def __init__(self, master):
        Frame.__init__(self, master)
        World().LOG().info("Frame called: " + self._myType)
        self._createWidgets()
        
        
    def _createWidgets(self):
        raise NotImplemented
        
        
    @staticmethod    
    def getInstance(master):
        raise NotImplemented
            