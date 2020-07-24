'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.Partner import PartnerManager

class Partner(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return PartnerManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return PartnerManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return PartnerManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return PartnerManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return PartnerManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return PartnerManager.getInstance().delete(partner)
    