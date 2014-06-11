'''
Created on 2014.03.05.

@author: fekete
'''

from copy import deepcopy

import tkinter.messagebox as mbox
from tkinter import END
from tkinter.constants import *
from tkinter import TclError
from tkinter.ttk import *
from builtins import NotImplemented

from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.gui.QuestionDialog import QuestionDialog
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class AbstractFrame(Frame):

    _instance = None
    _myTabId = 0
    _myElementId = 0
    _myEntityType = None
    _entity = None
    _storedEntity = None
    _type = 'Not Implemented'
    _myApplication = None
    _myListBox = None
    _myStoredListItems = None
    _myState = None
    _windowName = ''
    answer = None
    
    createButton = None
    editButton = None
    closeButton = None
    cancelButton = None
    deleteButton = None
    saveButton = None


    def __init__(self, master, appFrame, elementId=0):
        World().LOG().info("Frame called: " + self._type)
        Frame.__init__(self, master, padding= World.padSize())
        self._myApplication = appFrame
        self._myElementId = elementId
       
        
    def _cancel(self):
        World().LOG().info("_cancel called: " + str(self._entity.id) + "|" + self._entity.name)
        self.saveButtonEnabled(False)
        self.cancelButtonEnabled(False)
        self._displayElement(self._myElementId)


    def _clearForm(self):
        raise NotImplemented
    
    
    def _close(self):
        World().LOG().info("_close called: " + str(self._entity.id) + "|" + self._entity.name)

        if self._getState() == 'normal':
            self._handleChangeWhileInEditMode()
            
        if self.answer != 'ABORT':
            self._myListBox.delete(0, END)
            self.master.forget('current')
            if self.master.index('end') > 0:
                self.master.select('end')
            else:
                self.createButtonEnabled(False)
                self.closeButtonEnabled(False)
                self.saveButtonEnabled(False)
                self.cancelButtonEnabled(False)
                self.editButtonEnabled(False)
                self.deleteButtonEnabled(False)
                self._myApplication.exitButton.config(command=self._myApplication._onExit)
       
        self._myApplication.destroy()
                
                
    def _create(self):
        World().LOG().info("_create called: " + str(self._entity.id) + "|" + self._entity.name)

        self.createButtonEnabled(False)
        self.closeButtonEnabled(True)
        self.saveButtonEnabled(True)
        self.cancelButtonEnabled(True)
        self.editButtonEnabled(False)
        self.deleteButtonEnabled(False)
        self._myListBox.selection_clear(0, END)
        self.setState(self, 'normal')
        
        self._clearForm()

    

    def _createWidgets(self, r, c, cspan=0):
        buttonFrame = Frame(self)
        buttonFrame.grid(row=r, column=c, columnspan=cspan, sticky=E,
                         padx=World.smallPadSize(), pady=World.smallPadSize())
        
        self.createButton = Button(buttonFrame, text=World.L("CREATE"), state=DISABLED)
        self.createButton.pack(fill=BOTH, expand=1, side=LEFT,  padx=World.smallPadSize())

        self.editButton = Button(buttonFrame, text=World.L("MainWindow.EDIT"), state=DISABLED)
        self.editButton.pack(fill=BOTH, expand=1, side=LEFT,  padx=World.smallPadSize())
        
        self.saveButton = Button(buttonFrame, text=World.L("SAVE"), state=DISABLED)
        self.saveButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

        self.cancelButton = Button(buttonFrame, text=World.L("CANCEL"), state=DISABLED)
        self.cancelButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

        self.deleteButton = Button(buttonFrame, text=World.L("DELETE"), state=DISABLED)
        self.deleteButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

        self.closeButton = Button(buttonFrame, text=World.L("CLOSE"), state=DISABLED)
        self.closeButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

    
    def _delete(self):
        World().LOG().info("_delete called: " + str(self._entity.id) + "|" + self._entity.name)

        idx = int(self._myListBox.curselection()[0])
        new_idx = 0
        old_entity = deepcopy(self._entity)
        if idx > 0:
            new_idx = idx-1
        else:
            new_idx = idx
            
        self._displayElement(self._myStoredListItems[new_idx].id)    
                     
        self._myListBox.delete(idx)
        
        for item in self._myStoredListItems:
            if item.id == old_entity.id:
                self._myStoredListItems.remove(item)
                break
        self._myEntityType.delete(old_entity)
            
    
    def _displayElement(self, elementId):
        World().LOG().info("_displayElement called: " + str(elementId))

        if len(self._myStoredListItems) < 1:
            '''handle the empty datatable case'''
            self._create()
            return                
        
        self.answer = ''
        if self._getState() == 'normal' and elementId != self._myElementId:
            self._handleChangeWhileInEditMode()
            
        if self.answer != 'ABORT':
            self._myElementId = elementId

        idx = 0    
        if self._myElementId == 0:
            idx = 0
        else:
            for item in self._myStoredListItems:
                if item.id == self._myElementId:
                    break
                idx += 1
    
        if self.answer != 'ABORT':
            self.setState(self, 'normal')
            self.showItem(self._myStoredListItems[idx].id)
            self.setState(self, 'disabled')

        self._myListBox.selection_clear(0, END)        
        self._myListBox.selection_set(idx)
        
        
    def _edit(self):
        World().LOG().info("_edit called: " + str(self._entity.id) + "|" + self._entity.name)

        self.setState(self, 'normal')
        self.createButtonEnabled(False)
        self.saveButtonEnabled(True)
        self.cancelButtonEnabled(True)
        self.deleteButtonEnabled(False)
        
        
    def _getState(self):
        return self._myState
        
    
    def setState(self, widget, state='disabled'):
        World().LOG().info("setState called: " + state)

        if widget.winfo_class() == 'TLabel':
            return
        
        try:
            widget.configure(state=state)
        except TclError:
            pass
        
        for child in widget.winfo_children():
            if child.winfo_class() in ('TEntry', 'Text', 'TFrame', 'Button'):
                if child.winfo_class() != 'TFrame':
                    child.configure(state=state)
                                                    
                if  child.winfo_class() == 'Text':
                    if state == 'disabled':
                        child.configure(background=World.getDisabledBackgroundColor())
                        child.configure(foreground=World.getDisabledForegroundColor())
                    else:
                        child.configure(background=World.getNormalBackgroundColor())
                        child.configure(foreground=World.getNormalForegroundColor())
                        
        self._myState = state

    
    def _fillListWithElements(self):
        World().LOG().info("_fillListWithElement called.")

        self._myStoredListItems = self._myEntityType.getListItems()
        for e in self._myStoredListItems:
            self._myListBox.insert(END, e.name)

        self.createButtonEnabled(True)        
        self.editButtonEnabled(True)
        self.closeButtonEnabled(True)
        self.deleteButtonEnabled(True)
                
        
    def _handleChangeWhileInEditMode(self):
        World().LOG().info("_handleChangeWhileInEditMode called: " 
                           + str(self._entity.id) + "|" + self._entity.name)

        QuestionDialog(self,
                           title=World.L('QUESTION'),
                           message=World.L('AbstractFrame.ARC'),
                           cancelLabel=World.L('PROCEED_NO_SAVE'))
        if self.answer == 'SAVE':
            self._save()
        
        
    def _prepareSave(self):
        self._storedEntity = deepcopy(self._entity)
        self._save() # implemented in child panels
        
        
    def _save(self):
        World().LOG().info("_save called: " + str(self._entity.id) + "|" + self._entity.name)

        if self._validate() != None:
            return False
        
        self.createButtonEnabled(True)
        self.saveButtonEnabled(False)
        self.cancelButtonEnabled(False)
        self.deleteButtonEnabled(True)
        self.setState(self, 'disabled')
        
        if self._entity.id == 0:
            self._myEntityType.create(self._entity)
        else:
            self._myEntityType.update(self._entity)
        
        #refresh the listbox
        idx = 0
        self._myStoredListItems = self._myEntityType.getListItems()
        for item in self._myStoredListItems:
            if item.id == self._entity.id:
                if len(self._myListBox.curselection()) > 0:
                    self._myListBox.delete(self._myListBox.curselection()[0])
                self._myListBox.insert(idx, self._myStoredListItems[idx].name)
                break
            idx += 1
    
        self._myListBox.selection_set(idx)
        
        
    def _setControls(self):
        self.createButton.config(command=self._create)
        self.closeButton.config(command=self._close)
        self.cancelButton.config(command=self._cancel)
        self.deleteButton.config(command=self._delete)
        self.saveButton.config(command=self._prepareSave)
        self.editButton.config(command=self._edit)
        self._myApplication.exitButton.config(command=self._close)
        
 
    def showDialog(self, tabTitle):
        World().LOG().info("showDialog called: " + tabTitle)
        
        found = False
        oneTab = ''
        for oneTab in self._myApplication.noteBookPanel.tabs():
            if oneTab == self._windowName:
                found = True
                break
                       
        if found:
            self._myApplication.noteBookPanel.select(oneTab)
        else:
            self._myApplication.noteBookPanel.add(self, text=tabTitle)
            self._windowName =  self._myApplication.noteBookPanel.select()
            self._myListBox = self._myApplication.getListBox()
            self._myListBox.bind('<<ListboxSelect>>', self.refreshDetails)
            self._createWidgets()
            self._fillListWithElements()
                
        elementId = 0
        if self._entity != None:
            elementId = self._entity.id
            
        self._displayElement(elementId) # show or refresh data from DB 
        self._setControls()
 
        
    def _validate(self):
        raise NotImplemented
        
            
    def refreshDetails(self, params):
        selectedIdx = int(self._myListBox.curselection()[0])
        id = self._myStoredListItems[selectedIdx].id
        name = self._myStoredListItems[selectedIdx].name
        World().LOG().info("_refreshDetails called: idx=" + str(selectedIdx) 
                           + " id=" + str(id) + " name=" + name)
        self._displayElement(id)
    
        
    def showItem(self, elementId):
        raise NotImplemented
        
        
    @staticmethod    
    def getInstance(master):
        raise NotImplemented
       
    
    def createButtonEnabled(self, isEnabled):
        if isEnabled:
            self.createButton['state'] = NORMAL
        else:
            self.createButton['state'] = DISABLED
        
    def cancelButtonEnabled(self, isEnabled):
        if isEnabled:
            self.cancelButton['state'] = NORMAL
        else:
            self.cancelButton['state'] = DISABLED

    def closeButtonEnabled(self, isEnabled):
        if isEnabled:
            self.closeButton['state'] = NORMAL
        else:
            self.closeButton['state'] = DISABLED

    def editButtonEnabled(self, isEnabled):
        if isEnabled:
            self.editButton['state'] = NORMAL
        else:
            self.editButton['state'] = DISABLED

    def saveButtonEnabled(self, isEnabled):
        if isEnabled:
            self.saveButton['state'] = NORMAL
        else:
            self.saveButton['state'] = DISABLED

    def deleteButtonEnabled(self, isEnabled):
        if isEnabled:
            self.deleteButton['state'] = NORMAL
        else:
            self.deleteButton['state'] = DISABLED
