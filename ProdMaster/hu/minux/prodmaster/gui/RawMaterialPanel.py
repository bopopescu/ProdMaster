'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmaster.gui.AbstractFrame import AbstractFrame
from hu.minux.prodmaster.gui.MinuxTable import MinuxTable
from hu.minux.prodmaster.app.RawMaterial import RawMaterial
from hu.minux.prodmaster.app.RawMaterialContent import RawMaterialContent
from hu.minux.prodmaster.tools.World import World
# from hu.minux.prodmaster.gui.RawMaterialContentDialog import RawMaterialContentDialog


class RawMaterialPanel(AbstractFrame):

    _type = 'RAW_MATERIALS'
    _rawMaterialContentType = 'RAW_MATERIAL_CONTENT'
    _myEntityType = RawMaterial
    
    _nameLabel = None
    _nameEntry = None
    _isCompositeLabel = None
    _isCompositeEntry = None
    _contentLabel = None
    _contentTable = None
    _remarkLabel = None
    _remarkEntry = None
    

    def __init__(self, master, appFrame):
        AbstractFrame.__init__(self, master, appFrame)
        
        
    @staticmethod
    def getInstance(appFrame):
        if RawMaterialPanel._instance == None:
            RawMaterialPanel._instance = RawMaterialPanel(appFrame.getWorkPane(), appFrame)
        return RawMaterialPanel._instance


    def _clearForm(self):
        self._nameEntry.delete(0, END)
        self._isCompositeEntry.delete(0, END)
        self._contentTable.deleteEntries()
        self._remarkEntry.delete('0.0', END)
               
                   
    def _create(self):
        AbstractFrame._create(self)
        self._entity = RawMaterial.new()
        
                    
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
        self._isCompositeLabel = Label(self, text=World.L("IS_COMPOSITE"))
        self._isCompositeLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._isCompositeEntry = Entry(self, width=World.defaultEntryWidth())
        self._isCompositeEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        
        c = 0
        r += 1
        self._contentLabel = Label(self, text=World.L("CONTENTS"))
        self._contentLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        hd = (World.L('ID'), World.L('NAME'), World.L('%'), World.L('REMARK'))
        self._contentTable = MinuxTable(self, columns=4, header=hd, type=self._rawMaterialContentType)
        # self._contentTable.setInvisibleColumns((1,3, 7))
        self._contentTable.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
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
        

    def _editPerson(self, content):
        RawMaterialContentDialog(self, content)
        return content


    def setState(self, widget, state='disabled'):
        '''Override'''
        AbstractFrame.setState(self, widget, state)
        self._contentTable.setState(state)
        
        
    def _save(self):        
        self._entity.name = self._nameEntry.get()
        self._entity.is_composite = self._isCompositeEntry.get()
        self._entity.remark = self._remarkEntry.get('0.0', 'end-1c')
        
        if self._entity.is_composite:
            self._entity.contents = []
            contentData = self._contentTable.getAllData()
            for rowIdx in range(0, len(contentData)):
                rowData = self._contentTable.getRowData(rowIdx)
                content = RawMaterialContent.unserialize(rowData)
                self._entity.contents.append(content)
        
        AbstractFrame._save(self)


    def _validate(self):
        ''' TO BE IMPLEMENTED '''
        errorStr = None
        return errorStr
        
        
    def editChild(self, childType, data):
        World.LOG().info("editChild called: " + childType + " " + str(data))
        
        if childType == self._rawMaterialContentType:
            if len(data) == 0:
                data = [0, 0, '', self._entity.id, '', '', '', '']  
            content = RawMaterialContent.unserialize(data)
            content = self._editRawMaterialContent(content)
            if content.name != '': 
                data = RawMaterialContent.serialize(content)
            else:
                data = []
            
            if content.markedForDeletion:
                data[1] = MinuxTable.ENTITY_IS_MARKED_FOR_DELETION
        
        return data
            

    def refreshDetails(self, params):
        '''Override'''
        # self._contentTable.deleteEntries()
        AbstractFrame.refreshDetails(self, params)


    def showItem(self, elementId):
        self._entity = RawMaterial.get(elementId)
        e = self._entity
            
        self._clearForm()
        
        self._nameEntry.insert(0, e.name)
        self._isCompositeEntry.insert(0, e.is_composite)
        
        for content in e.contents:
            self._contentTable.appendRow(RawMaterialContent.serialize(content))
        
        self._remarkEntry.insert('0.0', e.remark)

