'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmain.dba.AdditiveGroup import AdditiveGroupManager
from hu.minux.prodmain.dba.DBEntity import DBEntity
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.dba.NameIdPair import NameIdPair


class Additive(DBEntity):

    name = ""
    e_number = ""
    additive_group = None    


class AdditiveManager(AbstractEntityManager):
    
    _instance = None
    
    MY_TABLE_NAME = "additive"
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
        self.additive_group = AdditiveGroupManager.getInstance().new()
    
    
    @staticmethod
    def getInstance():
        if AdditiveManager._instance == None:
            AdditiveManager._instance = AdditiveManager()
        return AdditiveManager._instance

        
    def new(self):
        return Additive()
        
        
    def create(self, e):
        sql = ("INSERT INTO " + self.MY_TABLE_NAME + " "
               "(name,  additive_group_id, e_number, remark) "
               "VALUES (%s, %s, %s, %s)")
        data = (e.name, e.additive_group.id, e.e_number, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid
         
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + self.MY_TABLE_NAME + ' WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = Additive()
        sql = ('SELECT id, name, additive_group_id, e_number, remark '
               'FROM '  + self.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, additive_group_id, e_number, remark) in res:
            e.id = id
            e.name = name
            e.additive_group = AdditiveGroupManager.getInstance().read(additive_group_id)
            e.e_number = e_number
            e.remark = remark
                
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE " + self.MY_TABLE_NAME + " SET name=%s, additive_group_id=%s, "
               "e_number=%s, remark=%s"
               "WHERE id=%s")
        data = (e.name, e.additive_group.id, e.e_number, e.remark, e.id)
        
        self.execute(sql, data)
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        sql = "DELETE FROM " + self.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True

    
    def readAll(self):        
        l = []
        sql = ("SELECT id, name, additive_group_id, e_number, remark "
               "FROM " + self.MY_TABLE_NAME + " "
               "ORDER BY name ASC")
      
        self.execute(sql)
        
        for (id, name, additive_group_nr, e_number, remark) in self._cursor:
            e = Additive()      
            e.id = id
            e.name = name
            e.additive_group_nr = additive_group_nr
            e.e_number = e_number
            e.remark = remark
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM " + self.MY_TABLE_NAME + " ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l

    