'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.app.AbstractModule import AbstractModule
from hu.minux.prodmaster.dba.Product import ProductManager


class Product(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return ProductManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return ProductManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return ProductManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return ProductManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return ProductManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return ProductManager.getInstance().delete(partner)
    