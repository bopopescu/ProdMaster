'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class Partner():

    id = 0
    name = ""
    reg_number = ""
    bank_account = ""
    head_city = ""
    head_zip = ""
    head_address = ""
    is_customer = False
    is_supplier = False
    remark = ""
     

class PartnerManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if PartnerManager._instance == None:
            PartnerManager._instance = PartnerManager()
        return PartnerManager._instance

        
    def new(self):
        return Partner()    
        
        
    def create(self, e):
        ### If already exists with the same name, enable it ###
        if e.id == 0:
            existingId = self.getIdByName(e)
            if existingId > 0:
                e.id = existingId
                return self.update(e)
        
        ### If the element does not already exists, we create it ###
        sql = ("INSERT INTO partner "
               "(name, reg_number, bank_account, head_city, head_zip, head_address, is_customer, is_supplier, remark, is_enabled) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (e.name, e.reg_number, e.bank_account, e.head_city, e.head_zip, e.head_address, e.is_customer, e.is_supplier, e.remark, 1)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        pid = 0
        sql = ('SELECT id FROM partner WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            pid = id
            break
        
        return pid
        
        
    def read(self, pid):       
        e = Partner()
        sql = ('SELECT id, name, reg_number, bank_account, head_city, head_zip, head_address, is_customer, is_supplier, remark '
               'FROM partner WHERE is_enabled=1 AND id = %s')
        
        self.execute(sql, (pid,))
        res = self._cursor.fetchall()
        
        for (id, name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark) in res:
            e.id = id 
            e.name = name
            e.reg_number = reg_number
            e.bank_account = bank_account
            e.head_city = head_city
            e.head_zip = head_zip
            e.head_address = head_address
            e.is_customer = customer
            e.is_supplier = supplier
            e.remark = remark
            break
        
        return e
            
 
         
    def update(self, e):        
        sql = ("UPDATE partner SET name=%s, reg_number=%s, bank_account=%s, head_city=%s, "
               "head_zip=%s, head_address=%s, is_customer=%s, is_supplier=%s, "
               "remark=%s, is_enabled=1 "
               "WHERE id=%s")
        data = (e.name, e.reg_number, e.bank_account,
                e.head_city, e.head_zip, e.head_address,
                e.is_customer, e.is_supplier, e.remark,
                e.id)
        
        self.execute(sql, data)
        self._db.conn.commit()
        
        return e

    
    def delete(self, e):        
        sql = "UPDATE partner SET is_enabled = 0 WHERE id=%s"
        self.execute(sql, (e.id,))
        self._db.conn.commit()
        return True

    
    def readAll(self):        
        l = []
        sql = ("SELECT id, name, reg_number, bank_account, head_city, head_zip, "
               "head_address, is_customer, is_supplier, remark "
               "FROM partner WHERE is_enabled=1 "
               "ORDER BY name ASC")
      
        self.execute(sql)
        
        for (id, name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark) in self._cursor:
            e = Partner()      
            e.id = id 
            e.name = self._cursor.name
            e.reg_number = self._cursor.reg_number
            e.bank_account = self._cursor.bank_account
            e.head_city = self._cursor.head_city
            e.head_zip = self._cursor.zip
            e.head_address = self._cursor.head_address
            e.is_customer = self._cursor.is_customer
            e.is_supplier = self._cursor.is_supplier
            e.remark = self._cursor.remark
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM partner WHERE is_enabled=1 ORDER BY name ASC"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    