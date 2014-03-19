'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.Menu import MenuManager

class Main(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getMainMenuItems():
        return MenuManager.getInstance().readAll()
    