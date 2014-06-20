'''
Created on 2014.06.20.

@author: fekete
'''

from hu.minux.prodmaster.gui.MinuxTable import MinuxTable
from hu.minux.prodmaster.tools.World import World


class ChooserTable(MinuxTable):

    
    def __init__(self, master, columns=2, rows=1,
                 header=('First header', 'Second header'),
                 type=None):
        MinuxTable.__init__(self, master, columns, rows, header, type)
        
        
    def _createControls(self):
        pass
        
