'''
Created on 2014.02.27.

@author: fekete
'''

from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.gui.AbstractWindow import AbstractWindow


class PersonDialog(AbstractWindow):
    
    __data = None
    
    __idEntry = None
    __nameEntry = None
    __addressEntry = None
    __phoneEntry = None
    __emailEntry = None
    __remarkEntry = None
    
    __person = None


    def __init__(self, master, person):
        Toplevel.__init__(self, master)
        World.LOG().info("PersonDialog opening.")
        self.title(World.L("PersonDialog.TITLE"))
        self['bd'] = World.padSize()
        self.__person = person

        self.__createWidgets()
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
        self.__nameEntry = Entry(self, width=World.defaultEntryWidth())
        self.__nameEntry.grid(row=r, column=c,
                             padx=World.smallPadSize(), pady=World.smallPadSize())

        r += 1
        c = 0
        addressLabel = Label(self, text=World.L("ADDRESS"))
        addressLabel.grid(row=r, column=c,
                           padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self.__addressEntry = Text(self, width=World.textEntryWidth(), height=4)
        self.__addressEntry.grid(row=r, column=c,
                                 padx=World.smallPadSize(), pady=World.smallPadSize())


        r += 1
        c = 0
        phoneLabel = Label(self, text=World.L("PHONE"))
        phoneLabel.grid(row=r, column=c,
                        padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self.__phoneEntry = Text(self, width=World.textEntryWidth(), height=4)
        self.__phoneEntry.grid(row=r, column=c,
                              padx=World.smallPadSize(), pady=World.smallPadSize())



        r += 1
        c = 0
        emailLabel = Label(self, text=World.L("EMAIL"))
        emailLabel.grid(row=r, column=c,
                        padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self.__emailEntry = Text(self, width=World.textEntryWidth(), height=4)
        self.__emailEntry.grid(row=r, column=c,
                              padx=World.smallPadSize(), pady=World.smallPadSize())

        r += 1
        c = 0
        remarkLabel = Label(self, text=World.L("REMARK"))
        remarkLabel.grid(row=r, column=c,
                         padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self.__remarkEntry = Text(self, width=World.textEntryWidth(), height=10)
        self.__remarkEntry.grid(row=r, column=c,
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
        
        deleteButton = Button(f, text=World.L('DELETE'), command=self.__markForDeletion)
        deleteButton.pack(side=LEFT, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        f.grid(row=r, column=c, columnspan=2, sticky=E,
               padx=World.smallPadSize(), pady=World.smallPadSize())
                
        self.center()
        self.resizable(False, False)


    def __markForDeletion(self):
        self.__person.markedForDeletion = True
        self.destroy()


    def __sendDataToMaster(self):
        self.__person.name = self.__nameEntry.get()
        self.__person.address = self.__addressEntry.get('0.0', 'end-1c')
        self.__person.phone = self.__phoneEntry.get('0.0', 'end-1c')
        self.__person.email = self.__emailEntry.get('0.0', 'end-1c')
        self.__person.remark = self.__remarkEntry.get('0.0', 'end-1c')
        self.destroy()
   
    
    def __showItem(self):
        self.__idEntry.config(text=self.__person.weight)
        self.__nameEntry.insert(0, self.__person.name)
        self.__addressEntry.insert('0.0', self.__person.address)
        self.__phoneEntry.insert('0.0', self.__person.phone)
        self.__emailEntry.insert('0.0', self.__person.email)
        self.__remarkEntry.insert('0.0', self.__person.remark)
        
