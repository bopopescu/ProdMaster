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
        self._translations = {'ABORT' : 'Megszakítás',
                              'ADDRESS': 'Cím',
                              'BANK_ACCOUNT_NUMBER': 'Bankszámlaszám',
                              'CANCEL': 'Mégsem',
                              'CLOSE': 'Bezárás',
                              'LOCATION': 'Település',
                              'LOGIN' : 'Belépés',
                              'NAME' : 'Név',
                              'PASSWORD' : 'Jelszó',
                              'PROCEED_NO_SAVE' : 'Folytatás mentés nélkül',
                              'QUESTION' : 'Kérdés',
                              'REG_NUMBER' : 'Adószám',
                              'REMARK': 'Megjegyzés',
                              'SAVE': 'Mentés',
                              'USERNAME' : 'Felhasználói név',
                              'ZIP': 'Irányítószám',
                              
                              'AbstractFrame.ARC' : 'Az űrlap szerkesztő módban van. Válasszon az alábbiak közül:', 

                              'Application.TITLE' : 'ProdMaster - MINUX Szoftver',
                              
                              'Exception.GENERAL' : 'Az alkalmazásban hiba lépett fel.\nTovábbi információt a naplófájlban talál.\n\nSTACKTRACE:\n',
                              'Exception.TITLE' : 'Alkalmazáshiba',
                              
                              'LoginDialog.TITLE' : 'Adja meg felhasználói adatait a belépéshez',
                              
                              'MainWindow.ADDITIVES' : 'Adalékanyagok',
                              'MainWindow.ADDITIVE_GROUPS' : 'Adalékanyag csoportok',
                              'MainWindow.DATA' : 'Törzsadatok',
                              'MainWindow.EDIT' : 'Szerkesztés',
                              'MainWindow.EXIT' : 'Kilépés',
                              'MainWindow.FILE' : 'Fájl',
                              'MainWindow.PARTNERS' : 'Partnerek',
                              'MainWindow.RAW_MATERIALS' : 'Alapanyagok',
                              '':''
                              }
                              
    
    @staticmethod
    def getInstance():
        if hu._instance == None:
            hu._instance = hu()
        return hu._instance          
