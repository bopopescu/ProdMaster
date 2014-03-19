'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class Partner(object):

    id = 0
    name = ""
    reg_number = ""
    bank_account = ""
    head_city = ""
    head_zip = ""
    head_address = ""
    customer = False
    supplier = False
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

        
    def create(self):               
        e = Partner() 
        sql = "INSERT INTO partner (name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark) \
               VALUES (%s, %s, %s, %s, %s, %s, %d, %d, %s)"
        data = (e.name, e.reg_number, e.bank_account, e.head_city, e.head_zip, e.head_address, e.customer, e.supplier, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.commit()

        return e
    
    
    def read(self, pid):       
        e = Partner()
        sql = "SELECT id, name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark FROM partner WHERE id = {0}".format(pid)
        
        self.execute(sql)
        res = self._cursor.fetchall()
        
        for (id, name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark) in res:
            e.id = id 
            e.name = name
            e.reg_number = reg_number
            e.bank_account = bank_account
            e.head_city = head_city
            e.head_zip = head_zip
            e.head_address = head_address
            e.customer = customer
            e.supplier = supplier
            e.remark = remark
            break
        
        return e
            

    def update(self, e):        
        sql = "UPDATE partner SET name=%s, reg_number=%s, bank_account=%s, head_city=%s, head_zip=%s, head_address=%s, customer=%d, supplier=%d, remark=%s \
               WHERE id = %d"
        data = (e.name, e.reg_number, e.bank_account, e.head_city, e.head_zip, e.head_address, e.customer, e.supplier, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.commit()
        
        return e

    
    def delete(self, id):        
        sql = "DELETE FROM partner WHERE id = %d"
        data = (id)
        self.execute(sql, data) 
        self._db.commit()
        
        return True

    
    def readAll(self):        
        l = []
        sql = "SELECT id, name, reg_number, bank_account, head_city, head_zip, head_address, customer, supplier, remark FROM partner order by name asc"
      
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
            e.customer = self._cursor.customer
            e.supplier = self._cursor.supplier
            e.remark = self._cursor.remark
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        l = []
        sql = "SELECT id, name FROM partner"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:
            pair = NameIdPair()    
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    