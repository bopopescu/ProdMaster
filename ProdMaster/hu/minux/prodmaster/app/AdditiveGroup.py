'''
Created on 2014.06.18.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.AdditiveGroup import AdditiveGroupManager

class AdditiveGroup(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return AdditiveGroupManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return AdditiveGroupManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return AdditiveGroupManager.getInstance().new()

    
    @staticmethod
    def update(additive_group):
        return AdditiveGroupManager.getInstance().update(additive_group)
    
    
    @staticmethod
    def create(additive_group):
        return AdditiveGroupManager.getInstance().create(additive_group)
 
    
    @staticmethod
    def delete(additive_group):
        return AdditiveGroupManager.getInstance().delete(additive_group)
    
    
    @staticmethod
    def serialize(additive_group):
        return AdditiveGroupManager.getInstance().serialize(additive_group)
    
    
    @staticmethod
    def unserialize(data):
        return AdditiveGroupManager.getInstance().unserialize(data)
    