#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014.02.26.

@author: fekete
'''

from hu.minux.prodmain.l10n.Translator import Translator


class hu(Translator):
    
    _instance = None

    def __init__(self):
        '''
        Constructor
        '''
        self._translations = {'ABORT' : 'Megszakítás',
                              'ADDITIVE_GROUP': 'Adalékcsoport',
                              'ADDRESS': 'Cím',
                              'BANK_ACCOUNT_NUMBER': 'Bankszámlaszám',
                              'BARCODE': 'Vonalkód',
                              'CANCEL': 'Mégsem',
                              'CLOSE': 'Bezárás',
                              'CONTACTS': 'Kapcsolattartók',
                              'CONTENTS': 'Összetevők',
                              'CREATE': 'Új létrehozása',
                              'DELETE': 'Törlés',
                              'EMAIL': 'Email',
                              'E_NUMBER': 'e-szám',
                              'ID': '#',
                              'IS_COMPOSITE': 'Összetett alapanyag',
                              'IS_END/IS_SEMI': 'Kész / félkész',
                              'LOCATION': 'Település',
                              'LOGIN' : 'Belépés',
                              'NAME' : 'Név',
                              'PASSWORD' : 'Jelszó',
                              'PHONE': 'Telefon',
                              'PROCEED_NO_SAVE' : 'Folytatás mentés nélkül',
                              'QUESTION' : 'Kérdés',
                              'REG_NUMBER' : 'Adószám',
                              'READY': 'Kész',
                              'REMARK': 'Megjegyzés',
                              'SAVE': 'Mentés',
                              'USERNAME' : 'Felhasználói név',
                              'ZIP': 'Irányítószám',
                              
                              'AbstractFrame.ARC' : 'Az űrlap szerkesztő módban van. Válasszon az alábbiak közül:', 

                              'Application.TITLE' : 'ProdMain - MINUX Szoftver',
                              
                              'Exception.GENERAL' : 'Az alkalmazásban hiba lépett fel.\nTovábbi információt a naplófájlban talál.\n\nSTACKTRACE:\n',
                              'Exception.TITLE' : 'Alkalmazáshiba',
                              
                              'LoginDialog.TITLE' : 'Adja meg felhasználói adatait a belépéshez',
                              
                              'MainWindow.ACCOUNT_CLASSES' : 'Számlaosztályok',
                              'MainWindow.ADDITIVES' : 'Adalékanyagok',
                              'MainWindow.ADDITIVE_GROUPS' : 'Adalékanyag csoportok',
                              'MainWindow.DATA' : 'Törzsadatok',
                              'MainWindow.EDIT' : 'Szerkesztés',
                              'MainWindow.EXIT' : 'Kilépés',
                              'MainWindow.FILE' : 'Fájl',
                              'MainWindow.MOVEMENTS' : 'Mozgások',
                              'MainWindow.MOVEMENT_TYPES' : 'Mozgásnemek',
                              'MainWindow.PARTNERS' : 'Partnerek',
                              'MainWindow.PRODUCTS' : 'Termékek',
                              'MainWindow.PURCHASE' : 'Vásárlás, beszerzés',
                              'MainWindow.RAW_MATERIALS' : 'Alapanyagok',
                              'MainWindow.ROUNDTRIP_SALES' : 'Túra értékesítés',
                              'MainWindow.STOCKS' : 'Raktárak',
                              'PersonDialog.TITLE' : 'Kapcsolat szerkesztése',
                              'MainWindow.TRANSACTIONS' : 'Tranzakciók',
                              '':''
                              }
                              
    
    @staticmethod
    def getInstance():
        if hu._instance == None:
            hu._instance = hu()
        return hu._instance          
