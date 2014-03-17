'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmaster.gui.AbstractFrame import AbstractFrame
from hu.minux.prodmaster.tools.World import World


class PartnerPanel(AbstractFrame):

    _myType = 'PARTNERS'
    
    _nameLabel = None
    _nameEntry = None
    _regNumberLabel = None
    _regNumber_Entry = None
    _bankAccountLabel = None
    _bankAccountEntry = None
    _headCityLabel = None
    _headCityEntry = None
    _headZipLabel = None
    _headZipEntry = None
    _headAddressLabel = None
    _headAddressEntry = None
    _remarkLabel = None
    _remarkEntry = None
    

    def __init__(self, master):
        AbstractFrame.__init__(self, master)
        
    
    @staticmethod
    def getInstance(master):
        if PartnerPanel._instance == None:
            PartnerPanel._instance = PartnerPanel(master)
        return PartnerPanel._instance
            
        
    def _createWidgets(self):
        
        r = 0
        c = 0
        self._nameLabel = Label(self, text=World.L("NAME"));
        self._nameLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._nameEntry = Entry(self, width=60)
        self._nameEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c = 0
        r += 1
        self._regNumberLabel = Label(self, text=World.L("REG_NUMBER"))
        self._regNumberLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._regNumberEntry = Entry(self, width=60)
        self._regNumberEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
       
        c = 0
        r += 1
        self._bankAccountLabel = Label(self, text=World.L("BANK_ACCOUNT_NUMBER"))
        self._bankAccountLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._bankAccountEntry = Entry(self, width=60)
        self._bankAccountEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        

        c = 0
        r += 1
        self._headCityLabel = Label(self, text=World.L("LOCATION"))
        self._headCityLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._headCityEntry = Entry(self, width=60)
        self._headCityEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c = 0
        r += 1
        self._headZipLabel = Label(self, text=World.L("ZIP"))
        self._headZipLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._headZipEntry = Entry(self, width=8)
        self._headZipEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c = 0
        r += 1
        self._headAddressLabel = Label(self, text=World.L("ADDRESS"))
        self._headAddressLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._headAddressEntry = Entry(self, width=60)
        self._headAddressEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        
        c = 0
        r += 1
        self._remarkLabel = Label(self, text=World.L("REMARK"))
        self._remarkLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._remarkEntry = Text(self, width=68, height=10)
        self._remarkEntry.grid(row=r, column=c, sticky="WE", padx=World.smallPadSize(), pady=World.smallPadSize())
        