'''
Created on 2014.06.18.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.RawMaterialContent import RawMaterialContentManager

class RawMaterialContent(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return RawMaterialContentManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return RawMaterialContentManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return RawMaterialContentManager.getInstance().new()

    
    @staticmethod
    def update(person):
        return RawMaterialContentManager.getInstance().update(person)
    
    
    @staticmethod
    def create(person):
        return RawMaterialContentManager.getInstance().create(person)
 
    
    @staticmethod
    def delete(person):
        return RawMaterialContentManager.getInstance().delete(person)
    
    
    @staticmethod
    def serialize(person):
        return RawMaterialContentManager.getInstance().serialize(person)
    
    
    @staticmethod
    def unserialize(data):
        return RawMaterialContentManager.getInstance().unserialize(data)
    