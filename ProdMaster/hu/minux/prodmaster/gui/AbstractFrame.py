'''
Created on 2014.03.05.

@author: fekete
'''

from tkinter import END
#from tkinter import Frame
from tkinter import TclError
from tkinter.ttk import *
from builtins import NotImplemented

from hu.minux.prodmaster.tools.World import World

class AbstractFrame(Frame):

    _instance = None
    _myEntity = None
    _myType = 'Not Implemented'
    _myApplication = None
    _myListBox = None
    _myStoredListItems = None


    def __init__(self, master, appFrame, elementId=0):
        Frame.__init__(self, master, padding= World.padSize())
        World().LOG().info("Frame called: " + self._myType)
        self._myApplication = appFrame
        self._myListBox = self._myApplication.getListBox()
        self._myListBox.bind('<<ListboxSelect>>', self.refreshDetails)
        self._createWidgets()
        self._fillListWithElements()
        self._displayElement(elementId) 
          

    def _displayElement(self, elementId):
        self._setState(self, 'normal')
        idx = 0
        
        if elementId == 0:
            idx = 0
        else:
            for item in self._myStoredListItems:
                if item.id == elementId:
                    break
                idx += 1
                
        self._myListBox.selection_set(idx)
        self.showItem(self._myStoredListItems[idx].id)
        self._setState(self, 'disabled')    
        
        
    def _createWidgets(self):
        raise NotImplemented
    
    
    def _setState(self, widget, state='disabled'):
        if widget.winfo_class() == 'TLabel':
            return
        try:
            widget.configure(state=state)
            print(widget.winfo_class())
        except TclError:
            pass
        for child in widget.winfo_children():
            if child.winfo_class() == 'TEntry' or child.winfo_class() == 'Text':
                child.configure(state=state)
                if  child.winfo_class() == 'Text':
                    if state == 'disabled':
                        child.configure(background=World.getDisabledBackgroundColor())
                        child.configure(foreground=World.getDisabledForegroundColor())
                    else:
                        child.configure(background=World.getNormalBackgroundColor())
                        child.configure(foreground=World.getNormalForegroundColor())

    
    def _fillListWithElements(self):
        self._myStoredListItems = self._myEntity.getListItems()
        for e in self._myStoredListItems:
            self._myListBox.insert(END, e.name)        
        
        self._myApplication.editButtonEnabled(True)
        self._myApplication.closeButtonEnabled(True)
            
    def refreshDetails(self, params):
        selectedIdx = int(self._myListBox.curselection()[0])
        self._displayElement(self._myStoredListItems[selectedIdx].id)
    
        
    def showItem(self, elementId):
        raise NotImplemented
        
        
    @staticmethod    
    def getInstance(master):
        raise NotImplemented
            