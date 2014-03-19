'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.Partner import PartnerManager

class Partner(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return PartnerManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def getPartner(elementId):
        return PartnerManager.getInstance().read(elementId)
    