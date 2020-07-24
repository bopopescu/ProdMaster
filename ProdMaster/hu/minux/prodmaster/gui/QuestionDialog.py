'''
Created on 2014.02.27.

@author: fekete
'''

import tkinter
from tkinter.ttk import *

from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.gui.AbstractWindow import AbstractWindow


class QuestionDialog(AbstractWindow):
    
    messageLabel = None
    abortButton = None
    saveButton = None
    cancelButton = None
    _main = None

    def __init__(self, main,
                 title='',
                 message='',
                 abortLabel=World.L("ABORT"),
                 saveLabel=World.L("SAVE"),
                 cancelLabel=World.L("CANCEL")):
        tkinter.Toplevel.__init__(self, main)
        self._main = main
        self['bd'] = World.padSize()
             
        c = 0
        r = 0
        
        messageLabel = Label(self, text=message)
        messageLabel.grid(row=r, column=c, columnspan=3, 
                          padx=World.padSize(), pady=World.padSize())

        r += 1
        abortButton = Button(self, text=abortLabel,
                             command= lambda:self._answer('ABORT'))
        abortButton.grid(row=r, column=c,
                         padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        saveButton = Button(self, text=saveLabel,
                            command= lambda:self._answer('SAVE'))
        saveButton.grid(row=r, column=c,
                        padx=World.smallPadSize(), pady=World.smallPadSize())

        c += 1
        cancelButton = Button(self, text=cancelLabel,
                              command= lambda:self._answer('CANCEL'))
        cancelButton.grid(row=r, column=c,
                           padx=World.smallPadSize(), pady=World.smallPadSize())
        
        self.center()
        self.resizable(False, False)
        self.setModal()


    def _answer(self, op):
        self._main.answer = op
        self.destroy()
