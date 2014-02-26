'''
Created on 2014.02.26.

@author: fekete
'''


class Translator(object):

    _translations = {}

    def __init__(self, params):
        pass
    
    def translate(self, string):
        try:
            return self._translations[string]
        except:
            pass
        
        return string
            