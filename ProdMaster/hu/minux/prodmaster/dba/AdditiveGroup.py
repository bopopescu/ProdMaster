'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.dba.DBEntity import DBEntity
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class AdditiveGroup(DBEntity):

    name = ""
    group_nr = 0


class AdditiveGroupManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if AdditiveGroupManager._instance == None:
            AdditiveGroupManager._instance = AdditiveGroupManager()
        return AdditiveGroupManager._instance

        
    def new(self):
        return AdditiveGroup()    
        
        
    def create(self, e):
        sql = ("INSERT INTO additive_group "
               "(name,  group_nr, remark) "
               "VALUES (%s, %s, %s)")
        data = (e.name, e.group_nr, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid
         
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM additive_group WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = AdditiveGroup()
        sql = ('SELECT id, name, group_nr, remark '
               'FROM additive_group WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, group_nr, remark) in res:
            e.id = id 
            e.name = name
            e.group_nr = group_nr
            e.remark = remark
            break
        
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE additive_group SET name=%s, group_nr=%s, "
               "remark=%s"
               "WHERE id=%s")
        data = (e.name, e.group_nr, e.remark, e.id)
        
        self.execute(sql, data)
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        sql = "DELETE FROM additive_group WHERE id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True

    
    def readAll(self):        
        l = []
        sql = ("SELECT id, name, group_nr, remark "
               "FROM additive_group "
               "ORDER BY name ASC")
      
        self.execute(sql)
        
        for (id, name, group_nr, remark) in self._cursor:
            e = AdditiveGroup()      
            e.id = id 
            e.name = self._cursor.name
            e.group_id = self._cursor.group_id
            e.remark = self._cursor.remark
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM additive_group ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    