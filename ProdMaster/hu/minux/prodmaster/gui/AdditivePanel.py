'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmain.gui.AbstractFrame import AbstractFrame
from hu.minux.prodmain.app.Additive import Additive
from hu.minux.prodmain.app.AdditiveGroup import AdditiveGroup
from hu.minux.prodmain.gui.ChooserTable import ChooserTable
from hu.minux.prodmain.gui.ChooserDialog import ChooserDialog
from hu.minux.prodmain.tools.World import World


class AdditivePanel(AbstractFrame):

    _type = 'ADDITIVE'
    _additiveGroupType = 'ADDITIVE_GROUP'
    _myEntityType = Additive
    
    _nameLabel = None
    _nameEntry = None
    _additiveGroupLabel = None
    _additiveGroupTable = None
    _eNumberLabel = None
    _eNumberEntry = None
    _remarkLabel = None
    _remarkEntry = None
    

    def __init__(self, main, appFrame):
        AbstractFrame.__init__(self, main, appFrame)
        
        
    @staticmethod
    def getInstance(appFrame):
        if AdditivePanel._instance == None:
            AdditivePanel._instance = AdditivePanel(appFrame.getWorkPane(), appFrame)
        return AdditivePanel._instance


    def _clearForm(self):
        self._nameEntry.delete(0, END)
        self._additiveGroupTable.deleteEntries()
        self._eNumberEntry.delete(0, END)
        self._remarkEntry.delete('0.0', END)
               
                   
    def _create(self):
        AbstractFrame._create(self)
        self._entity = Additive.new()
        
                    
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
        self._additiveGroupLabel = Label(self, text=World.L("ADDITIVE_GROUP"))
        self._additiveGroupLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        hd = (World.L('ID'), World.L('NAME'))
        self._additiveGroupTable = ChooserTable(self, columns=3, header=hd, type=self._additiveGroupType)
        self._additiveGroupTable.setInvisibleColumns((1,3,4))
        self._additiveGroupTable.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        
        c = 0
        r += 1
        self._eNumberLabel = Label(self, text=World.L("E_NUMBER"))
        self._eNumberLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._eNumberEntry = Entry(self, width=World.defaultEntryWidth())
        self._eNumberEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())        
        
        
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
        
        
    def editChild(self, childType, data):
        World.LOG().info("editChild called: " + childType + " " + str(data))
        
        if childType == self._additiveGroupType:
            if len(data) == 0:
                data = [0, 0, '', 0, '']  
            ag = AdditiveGroup.unserialize(data)
            ag = self._editAdditiveGroup(ag)
            if ag.name != '': 
                data = AdditiveGroup.serialize(ag)
            else:
                data = []
            
            if ag.markedForDeletion:
                data[1] = ChooserTable.ENTITY_IS_MARKED_FOR_DELETION
               
        return data


    def setState(self, widget, state='disabled'):
        '''Override'''
        self._additiveGroupTable.setState(state)
        AbstractFrame.setState(self, widget, state)
        
    
    def _editAdditiveGroup(self, ag):
        ChooserDialog(self, AdditiveGroup, ag) # ag contains only the name and id
        ag = AdditiveGroup.get(ag.id) # we should read the whole record
        self._entity.additive_group = ag
        World.LOG().debug("additive group choosen: " + str(ag.id))
        return ag
                
        
    def _save(self):        
        self._entity.name = self._nameEntry.get()
        # self._entity.additive_group = self._additiveGroupTable.get()
        self._entity.e_number = self._eNumberEntry.get() 
        self._entity.remark = self._remarkEntry.get('0.0', 'end-1c')
        
        AbstractFrame._save(self)


    def _validate(self):
        ''' TO BE IMPLEMENTED '''
        errorStr = None
        return errorStr
            

    def refreshDetails(self, params):
        '''Override'''
        # self._contactTable.deleteEntries()
        AbstractFrame.refreshDetails(self, params)


    def showItem(self, elementId):
        self._entity = Additive.get(elementId)
        e = self._entity
            
        self._clearForm()
        
        self._nameEntry.insert(0, e.name)
        self._eNumberEntry.insert(0, e.e_number)
        self._remarkEntry.insert('0.0', e.remark)
        
        self._additiveGroupTable.appendRow(AdditiveGroup.serialize(e.additive_group))

