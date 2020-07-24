'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmain.dba.DBEntity import DBEntity
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.dba.NameIdPair import NameIdPair


class RawMaterialContent(DBEntity):
    
    raw_material_id = 0
    percentage = 0
    
    MY_TABLE_NAME = 'raw_material_contents'
     

class RawMaterialContentManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if RawMaterialContentManager._instance == None:
            RawMaterialContentManager._instance = RawMaterialContentManager()
        return RawMaterialContentManager._instance

        
    def new(self):
        return RawMaterialContent()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + RawMaterialContent.MY_TABLE_NAME + " "
               "(raw_material_id, percentage, weight, remark) "
               "VALUES (%s, %s, %s, %s)")
        data = (e.raw_material_id, e.percentage, e.weight, e.remark)
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + RawMaterialContent.MY_TABLE_NAME + ' WHERE name = %s')
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):
        e = RawMaterialContent()
        sql = ('SELECT id, name, raw_material_id, remark, weight '
               'FROM ' + RawMaterialContent.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, raw_material_id, remark, weight) in res:
            e.id = id 
            e.name = name
            e.raw_material_id = raw_material_id
            e.remark = remark
            e.weight = weight
            break
        
        return e
 
         
    def update(self, e):
        raise NotImplemented

    
    def delete(self, e):        
        sql = "DELETE FROM " + RawMaterialContent.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True


    def deleteAllForRawMaterial(self, e):
        sql = "DELETE FROM " + RawMaterialContent.MY_TABLE_NAME + " WHERE raw_material_id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True
    
    
    def readAll(self):
        raise NotImplemented
    
    
    def readAllByRawMaterial(self, e):
        l = []
        sql = ('SELECT id, name, raw_material_id, percentage, remark, weight '
               'FROM ' + RawMaterialContent.MY_TABLE_NAME + ' ' 
               'WHERE raw_material_id = %s ORDER BY weight asc')
      
        self.execute(sql, (e.id,))
        res = self._cursor.fetchall()
        
        for (id, name, raw_material_id, percentage, remark, weight) in res:
            e = RawMaterialContent()
            e.id = id
            e.name = name
            e.raw_material_id = raw_material_id
            e.percentage = percentage
            e.remark = remark
            e.weight = weight
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        raise NotImplemented
    
    
    def serialize(self, e):
        data = []
        data.append(e.weight)
        data.append(e.id)
        data.append(e.raw_material_id)
        data.append(e.percentage)
        data.append(e.remark)
            
        return data
    
    
    def unserialize(self, data, e=None):
        if e == None:
            e = RawMaterialContent()  
            
        e.weight = data[0]
        e.id = data[1]
        e.raw_material_id = data[2]
        e.percentage = data[3]
        e.remark = data[4]
        
        return e
