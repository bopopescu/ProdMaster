'''
Created on 2014.03.05.

@author: fekete
'''

from tkinter import END
from tkinter import Frame
from builtins import NotImplemented

from hu.minux.prodmaster.tools.World import World

class AbstractFrame(Frame):

    _instance = None
    _myEntity = None
    _myType = 'Not Implemented'
    _myApplication = None
    _myListBox = None
    _myStoredListItems = None


    def __init__(self, master, appFrame):
        Frame.__init__(self, master, padx= World.padSize(), pady= World.padSize())
        World().LOG().info("Frame called: " + self._myType)
        self._myApplication = appFrame
        self._myListBox = self._myApplication.getListBox()
        self._myListBox.bind('<<ListboxSelect>>', self.refreshDetails)
        self._createWidgets()
        self._fillListWithElements()
        
        
    def _createWidgets(self):
        raise NotImplemented
    
    
    def _fillListWithElements(self):
        self._myStoredListItems = self._myEntity.getListItems()
        for e in self._myStoredListItems:
            self._myListBox.insert(END, e.name)
            
    def refreshDetails(self, params):
        selectedIdx = int(self._myListBox.curselection()[0])
        self.showItem(self._myStoredListItems[selectedIdx].id)
    
        
    def showItem(self, elementId):
        raise NotImplemented
        
        
    @staticmethod    
    def getInstance(master):
        raise NotImplemented
            