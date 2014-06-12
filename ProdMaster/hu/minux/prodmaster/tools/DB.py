'''
Created on 2014.02.22.

@author: fekete
'''

import logging
import mysql.connector
from mysql.connector import errorcode


class DB(object):

    __db = None
    conn = None
    cursor = None

    def __init__(self):                
        try:
            DB.conn = mysql.connector.connect(user='minux', password='nemerdekel',
                                               host='127.0.0.1',
                                               database='prodmaster',
                                               get_warnings=True)
            DB.cursor = DB.conn.cursor()
            logging.info("Database connection successful")
            return
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.exception("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.exception("Database does not exists")
            else:
                logging.exception(err)
 

    @staticmethod
    def getInstance():
        logging.info("DB.getConnection() called")
        #global _db
        if DB.__db == None:
            DB.__db = DB()
        return DB.__db
    
    @staticmethod
    def closeConnection():
        try:
            DB.cursor.close()
            DB.conn.close()
            logging.info("Database connection closed")
        except:
            logging.exception("Fatal exception while closing database connection")
 
 
    @staticmethod
    def execute(operation, params=None, multi=False):
        DB.cursor.execute(operation, params, multi)
        logging.debug(DB.cursor.statement)
            