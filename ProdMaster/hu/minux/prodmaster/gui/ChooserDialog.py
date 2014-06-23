'''
Created on 2014.02.27.

@author: fekete
'''

from copy import deepcopy

from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.gui.AbstractWindow import AbstractWindow


class ChooserDialog(AbstractWindow):
    
    __data = None
    
    __idEntry = None
    __nameListBox = None
    
    __myStoredListItems = None
    
    __appEntity = None
    
    __entity = None


    def __init__(self, master, appEntity, entity):
        Toplevel.__init__(self, master)
        World.LOG().info("ChooserDialog opening.")
        self.title(World.L("ChooserDialog.TITLE"))
        self['bd'] = World.padSize()
        self.__appEntity = appEntity
        self.__entity = entity

        self.__createWidgets()
        self.__fillListWithElements()
        self.__showItem()
        
        self.setModal()
        

    def __createWidgets(self):
        c = 0
        r = 0        

        idLabel = Label(self, text=World.L("ID"))
        idLabel.grid(row=r, column=c,
                       padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self.__idEntry = Label(self)
        self.__idEntry.grid(row=r, column=c,
                            padx=World.smallPadSize(), pady=World.smallPadSize())

        r += 1
        c = 0
        nameLabel = Label(self, text=World.L("NAME"))
        nameLabel.grid(row=r, column=c,
                       padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        f = Frame(self)
        scrollBar = Scrollbar(f)
        scrollBar.pack(side=RIGHT, fill=Y)
        self._nameListBox = Listbox(f, yscrollcommand=scrollBar.set,
                                    selectmode=SINGLE)
        self._nameListBox.pack(fill=BOTH, side=LEFT, expand=1)
        scrollBar.config(command=self._nameListBox.yview)
        f.grid(row=r, column=c,
               padx=World.smallPadSize(), pady=World.smallPadSize())

        ### BUTTONS ###
        r += 1
        c = 0
        f = Frame(self)
        readyButton = Button(f, text=World.L('READY'),
                             command=self.__sendDataToMaster)
        readyButton.pack(side=LEFT, padx=World.smallPadSize(), pady=World.smallPadSize())

        cancelButton = Button(f, text=World.L('CANCEL'), command=self.destroy)
        cancelButton.pack(side=LEFT, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        f.grid(row=r, column=c, columnspan=2, sticky=E,
               padx=World.smallPadSize(), pady=World.smallPadSize())
                
        self.center()
        self.resizable(False, False)


    def __fillListWithElements(self):
        self._myStoredListItems = self.__appEntity.getListItems()
        for e in self._myStoredListItems:
            self._nameListBox.insert(END, e.name)



    def __markForDeletion(self):
        pass


    def __sendDataToMaster(self):
        idx = int(self._nameListBox.curselection()[0])
        self.__entity.id = self._myStoredListItems[idx].id
        self.__entity.name = self._myStoredListItems[idx].name
        self.destroy()
   
    
    def __showItem(self):
        pass
        
