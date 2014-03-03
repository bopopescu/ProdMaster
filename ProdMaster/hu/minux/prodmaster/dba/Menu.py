'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.dba.AbstractEntityManager import AbstractEntityManager
from hu.minux.prodmaster.tools.World import World
from hu.minux.prodmaster.dba.NameIdPair import NameIdPair


class Menu(object):

    id = 0
    name = ""
    is_root = 0
    parent = ""
    weight = 0

     

class MenuManager(AbstractEntityManager):
    
    _instance = None
    
    def __init__(self):
        AbstractEntityManager.__init__(self)
    
    
    @staticmethod
    def getInstance():
        if MenuManager._instance == None:
            MenuManager._instance = MenuManager()
        return MenuManager._instance

        
    def create(self):               
        menu = Menu()
        sql = "INSERT INTO menu (name, is_root, parent, weight) VALUES (%s, %d, %s, %d)"
        data = (menu.name, menu.is_root, menu.parent, menu.weight)
        
        self.execute(sql, data)
        menu.id = self._cursor.lastrowid 
        self._db.commit()

        return menu
    
    
    def read(self, id):       
        menu = Menu()
        sql = "SELECT id, name, is_root, parent, weight FROM menu WHERE id = %d"
        data = (id)
        
        self.execute(sql, data)
        
        menu.id = self._cursor.id 
        menu.name = self._cursor.name
        menu.is_root = self._cursor.is_root
        menu.parent = self._cursor.parent
        menu.weight = self._cursor.weight
        
        return menu
            

    def update(self, menu):        
        sql = "UPDATE menu SET name = %s, is_root = %d, parent = %s, weight = %d WHERE id = %d"
        data = (menu.name, menu.is_root, menu.parent, menu.weight, menu.id)
        
        self.execute(sql, data)
        menu.id = self._cursor.lastrowid 
        self._db.commit()
        
        return menu

    
    def delete(self, id):        
        sql = "DELETE FROM menu WHERE id = %d"
        data = (id)
        self.execute(sql, data) 
        self._db.commit()
        
        return True

    
    def readAll(self):        
        menu = Menu()
        l = []
        sql = "SELECT id, name, is_root, parent, weight FROM menu"
      
        self.execute(sql)
        
        for (id, name, is_root, parent, weight) in self._cursor:      
            menu.id = id 
            menu.name = name
            menu.is_root = is_root
            menu.parent = parent
            menu.weight = weight
            
            l.append(menu)
        
        return l

    
    def readAllNameIdPairs(self):        
        pair = NameIdPair()
        l = []
        sql = "SELECT id, name FROM menu"
        
        self.execute(sql)
        
        for (id, name) in self._cursor:      
            pair.id = id 
            pair.name = name
            
            l.append(pair)
        
        return l
    