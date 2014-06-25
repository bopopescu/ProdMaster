'''
Created on 2014.06.18.

@author: fekete
'''

class DBEntity(object):

    id = 0;
    weight = 0
    remark = '' 
    markedForDeletion = False
    
    MY_TABLE_NAME = None
