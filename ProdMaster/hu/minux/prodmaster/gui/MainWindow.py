#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014.02.21.

@author: fekete
'''

from tkinter import *
from hu.minux.prodmaster.gui.PartnerPanel import PartnerPanel
from hu.minux.prodmaster.tools.World import World

class MainWindow(Frame):
 
    _mainPanedWindow = None   
    _leftPanel = None
    _rightPanel = None
    
    
    def _onExit(self):
        World.DBA().closeConnection()
        World.LOG().info("************** Application closed. Bye! **************\n")
        self.master.destroy()

            
    def _createPanel(self, panelType):
        
        if panelType == "PARTNER":
            World.LOG().info("PartnerPanel called")


        
    def _createPanels(self):
        self._mainPanedWindow = PanedWindow(orient=HORIZONTAL)
        self._mainPanedWindow.pack(fill=BOTH, expand=1)
        
        self._leftPanel = Canvas(self._mainPanedWindow, background="pink")
        self._mainPanedWindow.add(self._leftPanel, minsize=300)
        self._rightPanel = Canvas(self._mainPanedWindow, background="red")
        self._mainPanedWindow.add(self._rightPanel, minsize=500)


    def _createMenu(self):
        menubar = Menu(self.master)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label=World.L("MainWindow.EXIT"), command=self._onExit)
        menubar.add_cascade(label=World.L("MainWindow.FILE"), menu=fileMenu)
                
        editMenu = Menu(menubar)
        menubar.add_cascade(label=World.L("MainWindow.EDIT"), menu=editMenu)
        
        dataMenu = Menu(menubar)
        dataMenu.add_command(label=World.L("MainWindow.PARTNERS"), command=lambda:self._createPanel("PARTNER"))
        menubar.add_cascade(label=World.L("MainWindow.DATA"), menu=dataMenu)
    
        self.master.config(menu=menubar)
        
 
    def _createWidgets(self):        
        
        
        scrollBar = Scrollbar(self._leftPanel)
        scrollBar.pack(side=RIGHT, fill=Y)
        listBox = Listbox(self._leftPanel, yscrollcommand=scrollBar.set)
        listBox.pack(fill=BOTH, side=LEFT, expand=1)
        scrollBar.config(command=listBox.yview)


    def __init__(self, master=None):
        World.init()
        Frame.__init__(self, master)
        self.master.protocol("WM_DELETE_WINDOW", self._onExit)
        self._createMenu()
        self._createPanels()
        self._createWidgets()        
        
        
root = Tk()
root.title(World.L("Application.TITLE"))
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h-60))
root.minsize(800, 600)
app = MainWindow(master=root)
app.mainloop()
