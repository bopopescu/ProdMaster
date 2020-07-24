'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.dba.DBEntity import DBEntity
from hu.minux.prodmain.dba.TransactionItem import TransactionItem
from hu.minux.prodmain.dba.TransactionItem import TransactionItemManager
from hu.minux.prodmain.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.dba.NameIdPair import NameIdPair


class Transaction(DBEntity):

    name = ""
    is_composite = False
    contents = []
    
    MY_TABLE_NAME = 'raw_material'
     

class TransactionManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if TransactionManager._instance == None:
            TransactionManager._instance = TransactionManager()
        return TransactionManager._instance

        
    def new(self):
        return Transaction()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + Transaction.MY_TABLE_NAME + " "
               "(name, is_composite, remark) "
               "VALUES (%s, %s, %s)")
        data = (e.name, e.is_composite, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid
        
        if e.is_composite:
            TransactionItemManager.getInstance().deleteAllForTransaction(e)        
            for item in e.contents:
                TransactionItemManager.getInstance().create(item)
                
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + Transaction.MY_TABLE_NAME + ' WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = Transaction()
        sql = ('SELECT id, name, is_composite, remark '
               'FROM ' + Transaction.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, is_composite, remark) in res:
            e.id = id 
            e.name = name
            e.is_composite = is_composite
            e.remark = remark
            break
        
        if e.is_composite:
            e.contents = TransactionItemManager.getInstance().readAllByTransaction(e)
        
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE " + Transaction.MY_TABLE_NAME + " "
               "SET name=%s, is_composite=%s, "
               "remark=%s"
               "WHERE id=%s")
        data = (e.name, e.is_composite, e.remark,
                e.id)
        
        self.execute(sql, data)
                
        if e.is_composite:
            TransactionItemManager.getInstance().deleteAllForTransaction(e)
            for item in e.contents:
                TransactionItemManager.getInstance().create(item)
        
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        TransactionItemManager.getInstance().deleteAllForTransaction(e)

        sql = "DELETE FROM " + Transaction.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))        
        self._db.conn.commit()
        return True

    
    def readAll(self):
        raise NotImplemented

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM " + Transaction.MY_TABLE_NAME + " ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    