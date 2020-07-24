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


from hu.minux.prodmain.gui.AbstractWindow import AbstractWindow
from hu.minux.prodmain.gui.LoginDialog import LoginDialog
from hu.minux.prodmain.gui.AccountClassPanel import AccountClassPanel
from hu.minux.prodmain.gui.AdditivePanel import AdditivePanel
from hu.minux.prodmain.gui.AdditiveGroupPanel import AdditiveGroupPanel
from hu.minux.prodmain.gui.MovementTypePanel import MovementTypePanel
from hu.minux.prodmain.gui.PartnerPanel import PartnerPanel
from hu.minux.prodmain.gui.ProductPanel import ProductPanel
from hu.minux.prodmain.gui.RawMaterialPanel import RawMaterialPanel
from hu.minux.prodmain.gui.StockPanel import StockPanel
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.app.Main import Main


class MainWindow(AbstractWindow):
 
    _mainPanedWindow = None   
    _leftPanel = None
    noteBookPanel = None
    _listBox = None
    exitButton = None
    
    
    def __init__(self, main=None):
        World.init()
        Frame.__init__(self, main)
        Tk.report_callback_exception = self._show_error
        self.main.protocol("WM_DELETE_WINDOW", self._onExit)
        self._initStyles()
        self._login()
                     
           
    def _createLayout(self):
        
        self._mainPanedWindow = PanedWindow(orient=HORIZONTAL)
        self._mainPanedWindow.pack(fill=BOTH, expand=1)
        
        self._leftPanel = Canvas(self._mainPanedWindow, background="pink")
        self._mainPanedWindow.add(self._leftPanel)

        self.noteBookPanel = Notebook(self._mainPanedWindow)
        self._mainPanedWindow.add(self.noteBookPanel)
         
        buttonFrame = Frame()
        buttonFrame.pack(side=RIGHT, padx=World.smallPadSize(), pady=World.padSize())
        
        self.exitButton = Button(buttonFrame, text=World.L("MainWindow.EXIT"),
                                 command=self._onExit)
        self.exitButton.pack(fill=BOTH, expand=1, side=LEFT, padx=World.smallPadSize())
        

    def _createMenu(self):
        menubar = Menu(self.main, tearoff=0)
            
        menuItems = Main.getMainMenuItems()   
        for element in menuItems:
            World().LOG().debug("Menu item: " + element.name)
            if (element.is_root == True):
                newMenu = Menu(menubar, tearoff=0)
                menubar.add_cascade(label=World.L("MainWindow." + element.name),
                                    menu=newMenu)
                for item in menuItems:
                    if (item.is_root == False and item.parent == element.name):
                            com = "_on" + item.name.capitalize() 
                            function = getattr(self, com)
                            newMenu.add_command(label=World.L("MainWindow." 
                                                              + item.name),
                                                command=function) 
        self.main.config(menu=menubar)
        
 
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
        self.main.destroy()
  
  
    def _onPartners(self):   
        panel = PartnerPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.PARTNERS"))
    
    
    def _onAccount_classes(self):
        panel = AccountClassPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.ACCOUNT_CLASSES"))

    
    def _onAdditives(self):
        panel = AdditivePanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.ADDITIVES"))
    
    
    def _onAdditive_groups(self):
        panel = AdditiveGroupPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.ADDITIVE_GROUPS"))


    def _onMovement_types(self):
        panel = MovementTypePanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.MOVEMENT_TYPES"))


    def _onProducts(self):
        panel = ProductPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.PRODUCTS"))

    
    def _onRaw_materials(self):
        panel = RawMaterialPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.RAW_MATERIALS"))


    def _onStocks(self):
        panel = StockPanel.getInstance(self)
        panel.showDialog(World().L("MainWindow.STOCKS"))

    
    def _onPurchase(self):
        pass
        #panel = PurchasePanel.getInstance(self)
        #panel.showDialog(World().L("MainWindow.PURCHASE"))

    
    def _onRoundtrip_sales(self):
        pass
        #panel = RawMaterialPanel.getInstance(self)
        #panel.showDialog(World().L("MainWindow.RAW_MATERIALS"))

    

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
        
        
    def exitButtonEnabled(self, isEnabled):
        if isEnabled:
            self.exitButton['state'] = NORMAL
        else:
            self.exitButton['state'] = DISABLED

        
    def getListBox(self):
        return self._listBox
            

    def getWorkPane(self):
        return self.noteBookPanel
                
root = Tk()
root.title(World.L("Application.TITLE"))
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h-60))
root.geometry("1024x768")
root.minsize(800, 600)
mainApp = MainWindow(main=root)
root.mainloop()
