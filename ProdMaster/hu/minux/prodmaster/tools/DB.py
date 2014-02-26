'''
Created on 2014.02.22.

@author: fekete
'''

import logging
import mysql.connector
from mysql.connector import errorcode


class DB(object):

    _db = None
    _conn = None

    def __init__(self):                
        try:
            DB._conn = mysql.connector.connect(user='minux', password='nemerdekel',
                                               host='127.0.0.1',
                                               database='prodmaster')
            logging.info("Database connection successful")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.exception("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.exception("Database does not exists")
            else:
                logging.exception(err)
        else:
            DB._conn.close()    

    @staticmethod
    def getConnection():
        logging.info("DB.getConnection() called")
        #global _db
        if DB._db == None:
            DB._db = DB()
            
        return DB._db
    
    @staticmethod
    def closeConnection():
        try:
            DB._conn.close()
            logging.info("Database connection closed")
        except:
            logging.exception("Fatal exception while closing database connection")
            