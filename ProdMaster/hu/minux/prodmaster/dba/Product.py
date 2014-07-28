'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.DBEntity import DBEntity
from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class Product(DBEntity):

    name = ""
    is_end_product = False
    barcode = ""
    contents = []
    
    MY_TABLE_NAME = 'product'
     

class ProductManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if ProductManager._instance == None:
            ProductManager._instance = ProductManager()
        return ProductManager._instance

        
    def new(self):
        return Product()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + Product.MY_TABLE_NAME + " "
               "(name, is_endproduct, barcode, remark) "
               "VALUES (%s, %s, %s, %s)")
        data = (e.name, e.is_endproduct, e.barcode, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid
        
#         if e.is_composite:
#             RawMaterialContentManager.getInstance().deleteAllForRawMaterial(e)        
#             for item in e.contents:
#                 RawMaterialContentManager.getInstance().create(item)
                
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + Product.MY_TABLE_NAME + ' WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):       
        e = Product()
        sql = ('SELECT id, name, is_endproduct, barcode, remark '
               'FROM ' + Product.MY_TABLE_NAME + ' WHERE id = %s')
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, is_endproduct, barcode, remark) in res:
            e.id = id 
            e.name = name
            e.is_endproduct = is_endproduct
            e.barcode = barcode
            e.remark = remark
            break
        
#         if e.is_composite:
#             e.contents = RawMaterialContentManager.getInstance().readAllByRawMaterial(e)
        
        return e
 
         
    def update(self, e):        
        sql = ("UPDATE " + Product.MY_TABLE_NAME + " "
               "SET name=%s, is_endproduct=%s, "
               "barcode=%s, remark=%s "
               "WHERE id=%s")
        data = (e.name, e.is_endproduct, e.barcode, e.remark,
                e.id)
        
        self.execute(sql, data)
                
#         if e.is_composite:
#             RawMaterialContentManager.getInstance().deleteAllForRawMaterial(e)
#             for item in e.contents:
#                 RawMaterialContentManager.getInstance().create(item)
        
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
#        RawMaterialContentManager.getInstance().deleteAllForRawMaterial(e)

        sql = "DELETE FROM " + Product.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))        
        self._db.conn.commit()
        return True

    
    def readAll(self):
        raise NotImplemented

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM " + Product.MY_TABLE_NAME + " ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    