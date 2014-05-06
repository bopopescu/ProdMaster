#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014.02.21.

@author: fekete
'''

import traceback
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mbox


from hu.minux.prodmaster.gui.AbstractWindow import AbstractWindow
from hu.minux.prodmaster.gui.LoginDialog import LoginDialog
from hu.minux.prodmaster.gui.PartnerPanel import PartnerPanel
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.app.Main import Main


class MainWindow(AbstractWindow):
 
    _mainPanedWindow = None   
    _leftPanel = None
    _rightPanel = None
    _listBox = None
    editButton = None
    closeButton = None
    cancelButton = None
    saveButton = None
    
    
    def __init__(self, master=None):
        World.init()
        Frame.__init__(self, master)
        Tk.report_callback_exception = self._show_error
        self.master.protocol("WM_DELETE_WINDOW", self._onExit)
        self._initStyles()
        self._login()
                     
           
    def _createLayout(self):
        
        self._mainPanedWindow = PanedWindow(orient=HORIZONTAL)
        self._mainPanedWindow.pack(fill=BOTH, expand=1)
        
        self._leftPanel = Canvas(self._mainPanedWindow, background="pink")
        self._mainPanedWindow.add(self._leftPanel)

        self._rightPanel = Notebook(self._mainPanedWindow)
        self._mainPanedWindow.add(self._rightPanel)
         
        buttonFrame = Frame()
        buttonFrame.pack(side=RIGHT, padx=World.smallPadSize(), pady=World.padSize())
        
        self.editButton = Button(buttonFrame, text=World.L("MainWindow.EDIT"), state=DISABLED)
        self.editButton.pack(fill=BOTH, expand=1, side=LEFT,  padx=World.smallPadSize())
        
        self.saveButton = Button(buttonFrame, text=World.L("SAVE"), state=DISABLED)
        self.saveButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

        self.cancelButton = Button(buttonFrame, text=World.L("CANCEL"), state=DISABLED)
        self.cancelButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())

        self.closeButton = Button(buttonFrame, text=World.L("CLOSE"), state=DISABLED)
        self.closeButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())
        

    def _createMenu(self):
        menubar = Menu(self.master)
            
        menuItems = Main.getMainMenuItems()   
        for element in menuItems:
            if (element.is_root == True):
                newMenu = Menu(menubar)
                menubar.add_cascade(label=World.L("MainWindow." + element.name),
                                    menu=newMenu)
                for item in menuItems:
                    if (item.is_root == False and item.parent == element.name):
                            com = "_on" + item.name.capitalize() 
                            function = getattr(self, com)
                            newMenu.add_command(label=World.L("MainWindow." 
                                                              + item.name),
                                                command=function) 
        self.master.config(menu=menubar)
        
 
    def _createWidgets(self):                
        scrollBar = Scrollbar(self._leftPanel)
        scrollBar.pack(side=RIGHT, fill=Y)
        self._listBox = Listbox(self._leftPanel, yscrollcommand=scrollBar.set,
                                selectmode=SINGLE)
        self._listBox.pack(fill=BOTH, side=LEFT, expand=1)
        scrollBar.config(command=self._listBox.yview)


    def _initStyles(self):
        Style().map("TEntry",
                  foreground=[('disabled', World.getDisabledForegroundColor()),
                              ('active', World.getNormalForegroundColor())],
                  fieldbackground=[('disabled', World.getDisabledBackgroundColor())])
        
    
    def _login(self):
        LoginDialog(self)
   

    def _onExit(self):
        World.DBA().closeConnection()
        World.LOG().info("************** Application closed. Bye! **************\n")
        self.master.destroy()
  
  
    def _onPartners(self):   
        panel = PartnerPanel.getInstance(self)
        self._rightPanel.add(panel, text=World().L("MainWindow.PARTNERS"))
    
    
    def _onAdditives(self):
        raise NotImplemented
    
    
    def _onAdditive_groups(self):
        raise NotImplemented


    def _onRaw_materials(self):
        raise NotImplemented

    
    def _onSuccessfulLogin(self, loginWidget):
        loginWidget.destroy()
        self._createMenu()
        self._createLayout()
        self._createWidgets()
          
        
    def _show_error(self, *args):
        err = World().L("Exception.GENERAL")
        for elem in traceback.format_exception(*args):
            err += elem
        
        World().LOG().error(err)
        mbox.showerror(World().L('Exception.TITLE'), err)
        self._onExit()
        
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
        
    def getListBox(self):
        return self._listBox
            

    def getWorkPane(self):
        return self._rightPanel
                
root = Tk()
root.title(World.L("Application.TITLE"))
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h-60))
root.minsize(800, 600)
mainApp = MainWindow(master=root)
root.mainloop()
