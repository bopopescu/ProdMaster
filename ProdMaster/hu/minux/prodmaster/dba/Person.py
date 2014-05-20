'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class Person():

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
    contacts = []
     

class PersonManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if PersonManager._instance == None:
            PersonManager._instance = PersonManager()
        return PersonManager._instance

        
    def new(self):
        return Person()    
        
        
    def create(self, e):
        sql = ("INSERT INTO person "
               "(name, partner_id, address, phone, email, remark) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (e.name, e.partner_id, e.address, e.phone, e.email, e.remark)
        
        self.execute(sql, data)
        e.id = self._cursor.lastrowid 
        self._db.conn.commit()

        return e
    
    
    def getIdByName(self, e):
        pid = 0
        sql = ('SELECT id FROM person WHERE name = %s')        
        self.execute(sql, (e.name,))
        res = self._cursor.fetchall()
        
        for (id,) in res:
            pid = id
            break
        
        return pid
        
        
    def read(self, pid):
        e = Person()
        sql = ('SELECT id, name, partner_id, address, phone, email, remark '
               'FROM person WHERE id = %s')
        
        self.execute(sql, (pid,))
        res = self._cursor.fetchall()
        
        for (id, name, partner_id, address, phone, email, remark) in res:
            e.id = id 
            e.name = name
            e.partner_id = partner_id
            e.address = address
            e.phone = phone
            e.email = email
            e.remark = remark
            break
        
        return e
 
         
    def update(self, e):
        raise NotImplemented

    
    def delete(self, e):        
        sql = "DELETE FROM person WHERE partner_id=%s"
        self.execute(sql, (e.partner_id,))
        self._db.conn.commit()
        return True

    
    def readAll(self):
        raise NotImplemented
    
    
    def readAllByPartner(self, partner):
        l = []
        sql = ('SELECT id, name, partner_id, address, phone, email, remark '
               'FROM person WHERE partner_id = %s')
      
        self.execute(sql, (partner.id,))
        res = self._cursor.fetchall()
        
        for (id, name, partner_id, address, phone, email, remark) in res:
            e = Person()
            e.id = id
            e.name = name
            e.partner_id = partner_id
            e.address = address
            e.phone = phone
            e.email = email
            e.remark = remark
            
            l.append(e)
        
        return l

    
    def readAllNameIdPairs(self):        
        raise NotImplemented
    
    
    def serialize(self, person):
        data = []
        data.append(person.id)
        data.append(person.name)
        data.append(person.partner_id)
        data.append(person.address)
        data.append(person.phone)
        data.append(person.email)
        data.append(person.remark)
            
        return data
    
    
    def unserialize(self, data, person=None):
        if person == None:
            person = Person()
            
        person.id = data[0]
        person.name = data[1]
        person.partner_id = data[2]
        person.address = data[3]
        person.phone = data[4]
        person.email = data[5]
        person.remark = data[6]
        
        return person
