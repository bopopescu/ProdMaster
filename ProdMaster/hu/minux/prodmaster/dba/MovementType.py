'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.DBEntity import DBEntity
from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class MovementType(DBEntity):

    name = ""
    
    MY_TABLE_NAME = 'movement_type'
     

class MovementTypeManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if MovementTypeManager._instance == None:
            MovementTypeManager._instance = MovementTypeManager()
        return MovementTypeManager._instance

        
    def new(self):
        return MovementType()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + MovementType.MY_TABLE_NAME + " "
               "(name, remark) "
               "VALUES (%s, %s)")
        data = (e.name, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid        
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + MovementType.MY_TABLE_NAME + ' WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = MovementType()
        sql = ('SELECT id, name, remark '
               'FROM ' + MovementType.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, remark) in res:
            e.id = id 
            e.name = name
            e.remark = remark
            break
        
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE " + MovementType.MY_TABLE_NAME + " "
               "SET name=%s, "
               "remark=%s"
               "WHERE id=%s")
        data = (e.name, e.remark, e.id)
        
        self.execute(sql, data)                        
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        sql = "DELETE FROM " + MovementType.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))        
        self._db.conn.commit()
        return True

    
    def readAll(self):
        raise NotImplemented

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM " + MovementType.MY_TABLE_NAME + " ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    