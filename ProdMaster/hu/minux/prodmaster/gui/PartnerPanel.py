'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *
from tkinter.ttk import *

from hu.minux.prodmain.gui.AbstractFrame import AbstractFrame
from hu.minux.prodmain.gui.MinuxTable import MinuxTable
from hu.minux.prodmain.app.Partner import Partner
from hu.minux.prodmain.app.Person import Person
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.gui.PersonDialog import PersonDialog


class PartnerPanel(AbstractFrame):

    _type = 'PARTNERS'
    _personType = 'PERSON'
    _myEntityType = Partner
    
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
    _contactLabel = None
    _contactTable = None
    _remarkLabel = None
    _remarkEntry = None
    

    def __init__(self, main, appFrame):
        AbstractFrame.__init__(self, main, appFrame)
        
        
    @staticmethod
    def getInstance(appFrame):
        if PartnerPanel._instance == None:
            PartnerPanel._instance = PartnerPanel(appFrame.getWorkPane(), appFrame)
        return PartnerPanel._instance


    def _clearForm(self):
        self._nameEntry.delete(0, END)
        self._regNumberEntry.delete(0, END)
        self._bankAccountEntry.delete(0, END)
        self._headCityEntry.delete(0, END)
        self._headZipEntry.delete(0, END)
        self._headAddressEntry.delete(0, END)
        self._contactTable.deleteEntries()
        self._remarkEntry.delete('0.0', END)
               
                   
    def _create(self):
        AbstractFrame._create(self)
        self._entity = Partner.new()
        
                    
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
        self._regNumberLabel = Label(self, text=World.L("REG_NUMBER"))
        self._regNumberLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._regNumberEntry = Entry(self, width=World.defaultEntryWidth())
        self._regNumberEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
               
        c = 0
        r += 1
        self._bankAccountLabel = Label(self, text=World.L("BANK_ACCOUNT_NUMBER"))
        self._bankAccountLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._bankAccountEntry = Entry(self, width=World.defaultEntryWidth())
        self._bankAccountEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c = 0
        r += 1
        self._headCityLabel = Label(self, text=World.L("LOCATION"))
        self._headCityLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        self._headCityEntry = Entry(self, width=World.defaultEntryWidth())
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
        self._headAddressEntry = Entry(self, width=World.defaultEntryWidth())
        self._headAddressEntry.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        
        c = 0
        r += 1
        self._contactLabel = Label(self, text=World.L("CONTACTS"))
        self._contactLabel.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
        c += 1
        hd = (World.L('ID'), World.L('NAME'), World.L('ADDRESS'),
              World.L('PHONE'), World.L('EMAIL'))
        self._contactTable = MinuxTable(self, columns=6, header=hd, type=self._personType)
        self._contactTable.setInvisibleColumns((1,3, 7))
        self._contactTable.grid(row=r, column=c, sticky=W, padx=World.smallPadSize(), pady=World.smallPadSize())
        
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
        

    def _editPerson(self, person):
        PersonDialog(self, person)
        return person


    def setState(self, widget, state='disabled'):
        '''Override'''
        AbstractFrame.setState(self, widget, state)
        self._contactTable.setState(state)
        
        
    def _save(self):        
        self._entity.name = self._nameEntry.get()
        self._entity.reg_number = self._regNumberEntry.get()
        self._entity.bank_account = self._bankAccountEntry.get()
        self._entity.head_city = self._headCityEntry.get()
        self._entity.head_zip = self._headZipEntry.get()
        self._entity.head_address = self._headAddressEntry.get() 
        self._entity.is_customer = False
        self._entity.is_supplier = False
        self._entity.remark = self._remarkEntry.get('0.0', 'end-1c')
        
        self._entity.contacts = []
        contactData = self._contactTable.getAllData()
        for rowIdx in range(0, len(contactData)):
            rowData = self._contactTable.getRowData(rowIdx)
            person = Person.unserialize(rowData)
            self._entity.contacts.append(person)
        
        AbstractFrame._save(self)


    def _validate(self):
        ''' TO BE IMPLEMENTED '''
        errorStr = None
        return errorStr
        
        
    def editChild(self, childType, data):
        World.LOG().info("editChild called: " + childType + " " + str(data))
        
        if childType == self._personType:
            if len(data) == 0:
                data = [0, 0, '', self._entity.id, '', '', '', '']  
            person = Person.unserialize(data)
            person = self._editPerson(person)
            if person.name != '': 
                data = Person.serialize(person)
            else:
                data = []
            
            if person.markedForDeletion:
                data[1] = MinuxTable.ENTITY_IS_MARKED_FOR_DELETION
        
        return data
            

    def refreshDetails(self, params):
        '''Override'''
        # self._contactTable.deleteEntries()
        AbstractFrame.refreshDetails(self, params)


    def showItem(self, elementId):
        self._entity = Partner.get(elementId)
        p = self._entity
            
        self._clearForm()
        
        self._nameEntry.insert(0, p.name)
        self._regNumberEntry.insert(0, p.reg_number)
        self._bankAccountEntry.insert(0, p.bank_account)
        self._headCityEntry.insert(0, p.head_city)
        self._headZipEntry.insert(0, p.head_zip)
        self._headAddressEntry.insert(0, p.head_address)
        
        for contact in p.contacts:
            self._contactTable.appendRow(Person.serialize(contact))
        
        self._remarkEntry.insert('0.0', p.remark)

