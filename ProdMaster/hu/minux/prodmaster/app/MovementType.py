'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.MovementType import MovementTypeManager


class MovementType(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return MovementTypeManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return MovementTypeManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return MovementTypeManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return MovementTypeManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return MovementTypeManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return MovementTypeManager.getInstance().delete(partner)
    