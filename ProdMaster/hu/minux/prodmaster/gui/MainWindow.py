#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014.02.21.

@author: fekete
'''

import tkinter
from tkinter import Menu
from tkinter.ttk import * 


from hu.minux.prodmaster.gui.LoginDialog import LoginDialog
from hu.minux.prodmaster.gui.PartnerPanel import PartnerPanel
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.app.Main import Main

class MainWindow(Frame):
 
    _mainPanedWindow = None   
    _leftPanel = None
    _rightPanel = None
    
    
    def __init__(self, master=None):
        World.init()
        Frame.__init__(self, master)
        self.master.protocol("WM_DELETE_WINDOW", self._onExit)
        self._login()
                     

            
    def _createPanel(self, panelType):
        
        if panelType == "PARTNER":
            World.LOG().info("PartnerPanel called")

        
    def _createLayout(self):
        self._mainPanedWindow = PanedWindow(orient=tkinter.HORIZONTAL)
        self._mainPanedWindow.pack(fill=tkinter.BOTH, expand=1)
        
        self._leftPanel = tkinter.Canvas(self._mainPanedWindow, background="pink")
        self._mainPanedWindow.add(self._leftPanel)
        self._rightPanel = tkinter.Canvas(self._mainPanedWindow, background="red")
        self._mainPanedWindow.add(self._rightPanel)


    def _createMenu(self):
        menubar = Menu(self.master)
        
        for element in Main.getMainMenuItems():
            
            if (element.is_root == True):
                print (element.name)
            
            pass
            
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label=World.L("EXIT"), command=self._onExit)
        menubar.add_cascade(label=World.L("MainWindow.FILE"), menu=fileMenu)
                
        editMenu = Menu(menubar)
        menubar.add_cascade(label=World.L("MainWindow.EDIT"), menu=editMenu)
        
        dataMenu = Menu(menubar)
        dataMenu.add_command(label=World.L("MainWindow.PARTNERS"), command=lambda:self._createPanel("PARTNER"))
        dataMenu.add_command(label=World.L("MainWindow.RAW_MATERIALS"), command=lambda:self._createPanel("RAW_MATERIAL"))
        dataMenu.add_command(label=World.L("MainWindow.ADDITIVES"), command=lambda:self._createPanel("ADDITIVE"))
        dataMenu.add_command(label=World.L("MainWindow.ADDITIVE_GROUPS"), command=lambda:self._createPanel("ADDITIVE_GROUP"))
        menubar.add_cascade(label=World.L("MainWindow.DATA"), menu=dataMenu)
        self.master.config(menu=menubar)
        
 
    def _createWidgets(self):                
        scrollBar = Scrollbar(self._leftPanel)
        scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        listBox = tkinter.Listbox(self._leftPanel, yscrollcommand=scrollBar.set)
        listBox.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=1)
        scrollBar.config(command=listBox.yview)



    def _login(self):
        LoginDialog(self)
   

    def _onExit(self):
        World.DBA().closeConnection()
        World.LOG().info("************** Application closed. Bye! **************\n")
        self.master.destroy()

        
    def _onSuccessfulLogin(self, loginWidget):
        loginWidget.destroy()
        self._createMenu()
        self._createLayout()
        self._createWidgets()   
        
        
        
root = tkinter.Tk()
root.title(World.L("Application.TITLE"))
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h-60))
root.minsize(800, 600)
mainApp = MainWindow(master=root)
root.mainloop()

