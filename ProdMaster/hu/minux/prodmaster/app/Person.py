'''
Created on 2014.06.18.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.Person import PersonManager

class Person(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return PersonManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return PersonManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return PersonManager.getInstance().new()

    
    @staticmethod
    def update(person):
        return PersonManager.getInstance().update(person)
    
    
    @staticmethod
    def create(person):
        return PersonManager.getInstance().create(person)
 
    
    @staticmethod
    def delete(person):
        return PersonManager.getInstance().delete(person)
    
    
    @staticmethod
    def serialize(person):
        return PersonManager.getInstance().serialize(person)
    
    
    @staticmethod
    def unserialize(data):
        return PersonManager.getInstance().unserialize(data)
    