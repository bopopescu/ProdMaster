'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.AccountClass import AccountClassManager


class AccountClass(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return AccountClassManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return AccountClassManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return AccountClassManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return AccountClassManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return AccountClassManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return AccountClassManager.getInstance().delete(partner)
    