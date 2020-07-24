'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.dba.DBEntity import DBEntity
from hu.minux.prodmain.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.dba.NameIdPair import NameIdPair


class Stock(DBEntity):

    name = ""
    
    MY_TABLE_NAME = 'stock'
     

class StockManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if StockManager._instance == None:
            StockManager._instance = StockManager()
        return StockManager._instance

        
    def new(self):
        return Stock()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + Stock.MY_TABLE_NAME + " "
               "(name, remark) "
               "VALUES (%s, %s)")
        data = (e.name, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid        
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + Stock.MY_TABLE_NAME + ' WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = Stock()
        sql = ('SELECT id, name, remark '
               'FROM ' + Stock.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, remark) in res:
            e.id = id 
            e.name = name
            e.remark = remark
            break
        
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE " + Stock.MY_TABLE_NAME + " "
               "SET name=%s, "
               "remark=%s"
               "WHERE id=%s")
        data = (e.name, e.remark, e.id)
        
        self.execute(sql, data)                        
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        sql = "DELETE FROM " + Stock.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))        
        self._db.conn.commit()
        return True

    
    def readAll(self):
        raise NotImplemented

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM " + Stock.MY_TABLE_NAME + " ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    