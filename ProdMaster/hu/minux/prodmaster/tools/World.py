'''
Created on 2014.02.22.

@author: fekete
'''

import logging
from hu.minux.prodmaster.tools.DB import DB
from hu.minux.prodmaster.l10n.hu import hu

class World(object):

    _instance = None
    _DBA = None
    _logger = None


    def __init__(self):
        pass

    
    @staticmethod
    def init():
        try:
            logging.basicConfig(filename='prodmaster.log',
                                format='%(asctime)s %(levelname)s: %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                level=logging.DEBUG)
            World._logger = logging
            logging.info("\n************** Prodmaster application. Go ahead ! **************")    
        except Exception as e:
            print("Logging has not been started.")
            print(e)


        if World._instance == None:
            World._instance = World()
        World._DBA = DB.getInstance()        
    
    @staticmethod
    def DBA():
        if World._DBA == None:
            World._DBA = DB.getInstance()
 
        return World._DBA


    @staticmethod
    def defaultEntryWidth():
        return 60


    @staticmethod
    def getDisabledBackgroundColor():
        return 'gray95'


    @staticmethod
    def getDisabledForegroundColor():
        return 'gray10'

    
    @staticmethod
    def getNormalBackgroundColor():
        return 'white'


    @staticmethod
    def getNormalForegroundColor():
        return 'black'

    
    @staticmethod
    def L(string):
        if True: # TODO: language handling        
            return hu.getInstance().translate(string)


    @staticmethod
    def LOG():
        return World._logger

    
    @staticmethod
    def padSize():
        return 5
    
    
    @staticmethod
    def smallButtonWidth():
        return 3
    
    
    @staticmethod
    def smallPadSize():
        return 3
    
    @staticmethod
    def textEntryWidth():
        return 68
    


