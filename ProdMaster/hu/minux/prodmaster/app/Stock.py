'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.app.AbstractModule import AbstractModule
from hu.minux.prodmain.dba.Stock import StockManager


class Stock(AbstractModule):


    def __init__(self, params):
        pass
    
    
    @staticmethod
    def getListItems():
        return StockManager.getInstance().readAllNameIdPairs()


    @staticmethod
    def get(elementId):
        return StockManager.getInstance().read(elementId)

    
    @staticmethod
    def new():
        return StockManager.getInstance().new()

    
    @staticmethod
    def update(partner):
        return StockManager.getInstance().update(partner)
    
    
    @staticmethod
    def create(partner):
        return StockManager.getInstance().create(partner)
 
    
    @staticmethod
    def delete(partner):
        return StockManager.getInstance().delete(partner)
    