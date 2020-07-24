'''
Created on 2014.06.20.

@author: fekete
'''

from hu.minux.prodmain.gui.MinuxTable import MinuxTable
from hu.minux.prodmain.tools.World import World


class ChooserTable(MinuxTable):

    
    def __init__(self, main, columns=2, rows=1,
                 header=('First header', 'Second header'),
                 type=None):
        MinuxTable.__init__(self, main, columns, rows, header, type)
        
        
    def _createControls(self):
        pass
        
