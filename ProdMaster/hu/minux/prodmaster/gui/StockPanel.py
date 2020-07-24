'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmain.gui.AbstractFrame import AbstractFrame
from hu.minux.prodmain.gui.MinuxTable import MinuxTable
from hu.minux.prodmain.app.Stock import Stock
from hu.minux.prodmain.tools.World import World


class StockPanel(AbstractFrame):

    _type = 'STOCKS'
    _myEntityType = Stock
    
    _nameLabel = None
    _nameEntry = None
    _remarkLabel = None
    _remarkEntry = None
    

    def __init__(self, main, appFrame):
        AbstractFrame.__init__(self, main, appFrame)
        
        
    @staticmethod
    def getInstance(appFrame):
        if StockPanel._instance == None:
            StockPanel._instance = StockPanel(appFrame.getWorkPane(), appFrame)
        return StockPanel._instance


    def _clearForm(self):
        self._nameEntry.delete(0, END)
        self._remarkEntry.delete('0.0', END)
               
                   
    def _create(self):
        AbstractFrame._create(self)
        self._entity = Stock.new()
        
                    
    def _createWidgets(self):
        
        r = 0
        c = 0
        self._nameLabel = Label(self, text=World.L("NAME"));
        self._nameLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._nameEntry = Entry(self, width=World.defaultEntryWidth())
        self._nameEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
                
        c = 0
        r += 1
        self._remarkLabel = Label(self, text=World.L("REMARK"))
        self._remarkLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._remarkEntry = Text(self, width=World.textEntryWidth(), height=10)
        self._remarkEntry.grid(row=r, column=c, sticky="WE", padx=World.smallPadSize(), pady=World.smallPadSize())
        
        # Append operation buttons
        c = 0
        r += 1
        AbstractFrame._createWidgets(self, r , c, 2)
        

    def setState(self, widget, state='disabled'):
        '''Override'''
        AbstractFrame.setState(self, widget, state)
        
        
    def _save(self):        
        self._entity.name = self._nameEntry.get()
        self._entity.remark = self._remarkEntry.get('0.0', 'end-1c')
        
        AbstractFrame._save(self)


    def _validate(self):
        ''' TO BE IMPLEMENTED '''
        errorStr = None
        return errorStr
                    

    def refreshDetails(self, params):
        '''Override'''
        # self._contentTable.deleteEntries()
        AbstractFrame.refreshDetails(self, params)


    def showItem(self, elementId):
        self._entity = Stock.get(elementId)
        e = self._entity
            
        self._clearForm()
        
        self._nameEntry.insert(0, e.name)
        self._remarkEntry.insert('0.0', e.remark)
