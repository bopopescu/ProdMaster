#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014.02.26.

@author: fekete
'''

from hu.minux.prodmaster.l10n.Translator import Translator


class hu(Translator):
    
    _instance = None

    def __init__(self):
        '''
        Constructor
        '''
        self._translations = {'Application.TITLE' : 'ProdMaster - MINUX Szoftver',
                              
                              'MainWindow.DATA' : 'Törzsadatok',
                              'MainWindow.EDIT' : 'Szerkesztés',
                              'MainWindow.EXIT' : 'Kilépés',
                              'MainWindow.FILE' : 'Fájl',
                              'MainWindow.PARTNERS' : 'Partnerek',
                              '':''
                              }
                              
    
    @staticmethod
    def getInstance():
        if hu._instance == None:
            hu._instance = hu()
        return hu._instance          
