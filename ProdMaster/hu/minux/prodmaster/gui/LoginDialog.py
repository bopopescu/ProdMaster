'''
Created on 2014.02.27.

@author: fekete
'''

import tkinter
from tkinter import *

from hu.minux.prodmaster.tools.World import World


class LoginDialog(Toplevel):
    
    _nameEntry = None
    _passwordEntry = None

    def __init__(self, master):
        tkinter.Toplevel.__init__(self, master)
        World.LOG().info("Login process started.")
        self.protocol("WM_DELETE_WINDOW", master._onExit)
        self['bd'] = World.padSize()
             
        c = 0
        r = 0        
        
        titleLabel = Label(self, text=World.L("LoginDialog.TITLE"))
        titleLabel.grid(row=r, column=c, columnspan=2, 
                        padx=World.padSize(), pady=World.padSize())

        r += 1
        nameLabel = Label(self, text=World.L("USERNAME"))
        nameLabel.grid(row=r, column=c,
                       padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self._nameEntry = Entry(self)
        self._nameEntry.grid(row=r, column=c,
                             padx=World.smallPadSize(), pady=World.smallPadSize())

        r += 1
        c = 0
        passwordLabel = Label(self, text=World.L("PASSWORD"))
        passwordLabel.grid(row=r, column=c,
                           padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        self._passwordEntry = Entry(self)
        self._passwordEntry.grid(row=r, column=c,
                                 padx=World.smallPadSize(), pady=World.smallPadSize())

        r += 1
        c = 0
        loginButton = Button(self, text=World.L('LOGIN'),
                             command=lambda: master._onSuccessfulLogin(self))
        loginButton.grid(row=r, column=c,
                         padx=World.smallPadSize(), pady=World.smallPadSize())
        c += 1
        exitButton = Button(self, text=World.L('EXIT'), command=master._onExit)
        exitButton.grid(row=r, column=c,
                        padx=World.smallPadSize(), pady=World.smallPadSize())
        
        sw, sh = master.winfo_screenwidth(), master.winfo_screenheight()
        self.geometry("+%d+%d" % (sw/3, sh/3))
        
        self.resizable(False, False)        
        self.focus()
        self.lift(master)