'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.RawMaterial import RawMaterialManager


class RawMaterial(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return RawMaterialManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return RawMaterialManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return RawMaterialManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return RawMaterialManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return RawMaterialManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return RawMaterialManager.getInstance().delete(partner)
    