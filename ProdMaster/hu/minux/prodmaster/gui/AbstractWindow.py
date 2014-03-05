'''
Created on 2014.03.03.

@author: fekete
'''

from tkinter import Toplevel

from hu.minux.prodmaster.tools.World import World


class AbstractWindow(Toplevel):


    def __init__(self, master):
        Toplevel.__init__(self, master)
        pass
    
    
    def setModal(self):
        self.focus()
        self.lift(self.master)
        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)
        
        
    def center(self):
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        self_width =  width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        self_height = height + titlebar_height + frm_width
        x = self.master.winfo_screenwidth() // 2 - self_width // 2
        y = self.master.winfo_screenheight() // 2 - self_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        if self.attributes('-alpha') == 0:
            self.attributes('-alpha', 1.0)
        self.deiconify()
