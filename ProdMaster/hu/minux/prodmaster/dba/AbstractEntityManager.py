'''
Created on 2014.03.01.

@author: fekete
'''

from hu.minux.prodmaster.tools.World import World


class AbstractEntityManager(object):

    _db = None
    _cursor = None


    def __init__(self):
        World.LOG().info("AbstractEntityManager constructor called")
        self._db = World.DBA()
        self._cursor = self._db.cursor


    def execute(self, operation, params=None, multi=False):
        self._db.execute(operation, params, multi)
        

    def new(self):
        raise NotImplemented

    def create(self):
        raise NotImplemented
    
    def read(self, id):
        raise NotImplemented    

    def update(self, dbobject):
        raise NotImplemented
    
    def delete(self, id):
        raise NotImplemented
    
    def readAll(self):
        raise NotImplemented
    
    def readAllNameIdPairs(self):
        raise NotImplemented
    