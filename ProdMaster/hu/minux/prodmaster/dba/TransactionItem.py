'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmain.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmain.dba.DBEntity import DBEntity
from hu.minux.prodmain.tools.World import World
from hu.minux.prodmain.dba.NameIdPair import NameIdPair
from hu.minux.prodmain.dba.RawMaterial import RawMaterialManager
from hu.minux.prodmain.dba.Product import ProductManager
from hu.minux.prodmain.dba.Transaction import TransactionManager
from hu.minux.prodmain.dba.AccountClass import AccountClassManager
from hu.minux.prodmain.dba.Product import ProductManager


class TransactionItem(DBEntity):
    
    name = ""
    raw_material = None
    product = None
    transaction = None
    account_class = None
    stock = None
    unit = None
    quantity = 0
    value_net = 0
    tax_rate = 0
    value_gross = 0    
    
    MY_TABLE_NAME = 'transaction_item'
     

class TransactionItemManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if TransactionItemManager._instance == None:
            TransactionItemManager._instance = TransactionItemManager()
        return TransactionItemManager._instance

        
    def new(self):
        return TransactionItem()    
        
        
    def create(self, e):
        sql = ("INSERT INTO " + TransactionItem.MY_TABLE_NAME + " "
               "(name, raw_material_id, product_id, transaction_id, account_class_id, stock_id"
               "unit, quantity, value_net, tax_rate, value_gross, remark) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (e.name, e.raw_material.id, e.product.id, e.transaction.id, e.account_class.id, e.stock.id,
                e.unit.name, e.quantity, e.value_net, e.tax_rate, e.value_gross, e.remark)
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        eid = 0
        sql = ('SELECT id FROM ' + TransactionItem.MY_TABLE_NAME + ' WHERE name = %s')
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            eid = id
            break
        
        return eid
        
        
    def read(self, eid):
        e = TransactionItem()
        sql = ("SELECT name, raw_material_id, product_id, transaction_id, account_class_id, stock_id, "
               "unit, quantity, value_net, tax_rate, value_gross, remark "
               "FROM " + TransactionItem.MY_TABLE_NAME + " WHERE id = %s")
        
        self.execute(sql, (eid,))
        res = self._cursor.fetchall()
        
        for (id, name, raw_material_id, product_id, transaction_id, account_class_id, stock_id,
             unit, quantity, value_net, tax_rate, value_gross, remark, weight) in res:
            e.id = id 
            e.name = name
            e.raw_material = raw_material_id
            e.product = product_id
            e.transaction = transaction_id
            e.account_class = account_class_id
            e.stock = stock_id
            e.unit = unit
            e.quantity = quantity
            e.value_net = value_net
            e.tax_rate = tax_rate
            e.value_gross = value_gross            
            e.remark = remark
            e.weight = weight
            break
        
        return e
 
         
    def update(self, e):
        raise NotImplemented

    
    def delete(self, e):        
        sql = "DELETE FROM " + TransactionItem.MY_TABLE_NAME + " WHERE id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True


    def deleteAllForTransaction(self, e):
        sql = "DELETE FROM " + TransactionItem.MY_TABLE_NAME + " WHERE transaction_id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True
    
    
    def readAll(self):
        raise NotImplemented
    
    
    def readAllByTransaction(self, e):
        l = []
        sql = ("SELECT name, raw_material_id, product_id, transaction_id, account_class_id, stock_id, "
               "unit, quantity, value_net, tax_rate, value_gross, remark "
               "FROM " + TransactionItem.MY_TABLE_NAME + " " 
               'WHERE transaction_id = %s ORDER BY weight asc')
      
        self.execute(sql, (e.id,))
        res = self._cursor.fetchall()
        
        for (id, name, raw_material_id, product_id, transaction_id, account_class_id, stock_id,
             unit, quantity, value_net, tax_rate, value_gross, remark, weight) in res:
            e = TransactionItem()
            e.id = id 
            e.name = name
            e.raw_material = RawMaterialManager.getInstance().read(raw_material_id)
            e.product = ProductManager.getInstance().read(product_id)
            e.transaction = TransactionManager.getInstance().read(transaction_id)
            e.account_class = AccountClassManager.getInstance().read(account_class_id)
            e.stock = None #StockManager.getInstance().read(stock_id)
            e.unit = unit
            e.quantity = quantity
            e.value_net = value_net
            e.tax_rate = tax_rate
            e.value_gross = value_gross            
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
        data.append(e.raw_material.id)
        data.append(e.product.id)
        data.append(e.transaction.id)
        data.append(e.account_class.id)
        data.append(e.stock.id)
        data.append(e.unit)
        data.append(e.quantity)
        data.append(e.value_net)
        data.append(e.tax_rate)
        data.append(e.value_gross)
        data.append(e.remark)
            
        return data
    
    
    def unserialize(self, data, e=None):
        if e == None:
            e = TransactionItem()  
            
        e.weight = data[0]
        e.id = data[1]
        e.raw_material = RawMaterialManager.getInstance().read(data[2])
        e.product = ProductManager.getInstance().read(data[3])
        e.transaction = TransactionManager.getInstance().read(data[4])
        e.account_class = AccountClassManager.getInstance().read(data[5])
        e.stock = None #StockManager.getInstance().read(data[6])
        e.unit = data[7]
        e.quantity = data[8]
        e.value_net = data[9]
        e.tax_rate = data[10]
        e.value_gross = data[11]
        e.remark = data[12]
        
        return e
