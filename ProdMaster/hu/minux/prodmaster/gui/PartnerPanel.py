'''
Created on 2014.02.21.

@author: fekete
'''


from tkinter import *

from hu.minux.prodmaster.gui.AbstractFrame import AbstractFrame

class PartnerPanel(AbstractFrame):

    _myType = 'PARTNERS'

    def __init__(self, master):
        AbstractFrame.__init__(self, master)
        
    
    @staticmethod
    def getInstance(master):
        if PartnerPanel._instance == None:
            PartnerPanel._instance = PartnerPanel(master)
        return PartnerPanel._instance
            
        
    def _createWidgets(self):
        pass
    
    