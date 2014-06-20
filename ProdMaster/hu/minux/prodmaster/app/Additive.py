'''
Created on 2014.06.18.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.Additive import AdditiveManager

class Additive(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return AdditiveManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return AdditiveManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return AdditiveManager.getInstance().new()

    
    @staticmethod
    def update(additive):
        return AdditiveManager.getInstance().update(additive)
    
    
    @staticmethod
    def create(additive):
        return AdditiveManager.getInstance().create(additive)
 
    
    @staticmethod
    def delete(additive):
        return AdditiveManager.getInstance().delete(additive)
    
    
    @staticmethod
    def serialize(additive):
        return AdditiveManager.getInstance().serialize(additive)
    
    
    @staticmethod
    def unserialize(data):
        return AdditiveManager.getInstance().unserialize(data)
    