'''
Created on 2014.05.14.

@author: fekete
'''

from tkinter.ttk import *

from hu.minux.prodmaster.tools.World import World


class MinuxTable(Frame):
    '''
    classdocs
    '''

    __data = None
    __header = None
    __type = None ### id to callback master panel
    __rows = None
    __columnCount = 0
    __invisibleColumns = ()
    __plusButton = None
    __widgets = []
    __widgetFrame = None


    def __init__(self, master, columns=2, rows=1, header=('First header', 'Second header'),
                 type=None):
        Frame.__init__(self, master, padding=World.padSize())

        self.__type = type

        self.__columnCount = columns
        self.__data = []
        
        self.__createGrid()
        self.setHeader(header)        
        self.__createControls()
        

    def __createControls(self):
        self.__plusButton = Button(self, text='+', 
                                   width=World.smallButtonWidth())
        self.__plusButton.grid(row=1, column=0,
                               padx=World.smallPadSize(),
                               pady=World.smallPadSize(),
                               sticky="SW")

        
    def __createGrid(self):
        self.__widgetFrame = Frame(self)
        self.__widgetFrame.grid(row=0, column=0)
        for r in range(self.getRowCount()):
            self.appendRow(self.__data[r])

            
    def __editRow(self, data):
        newData = self.master.editChild(self.__type, data)
        rowIdx = 0
        for actualRow in self.__widgets:
            if rowIdx > 0:
                if str(actualRow[0]['text']) == str(newData[0]):
                    self.setRowData(rowIdx, newData)
                    break
            rowIdx += 1
        
        
    def clear(self):
        return
        World.LOG().info("MinuxTable.clear() called")
        for widget in self.__widgetFrame.grid_slaves():
            widget.grid_forget()
            widget.destroy()

        del self.__widgets[1:]
        del self.__data[:]
     
        
    def deleteEntries(self):
        '''do not remove the header'''
        r = 0
        for row in self.__widgets:            
            if r > 0:
                for widget in row:
                    widget.grid_forget()
            r += 1
            
        del self.__widgets[1:]
        del self.__data[:]
        
                
    def setHeader(self, header):
        '''header: a list of strings with names of columns'''
        self.appendRow(header)
        self.__header = header
    
    
    def getColumnCount(self):
        return self.__columnCount
    
    
    def getDataInRow(self, rowIndex):
        if self.__data != None and len(self.__data) >= rowIndex:
            return self.__data[rowIndex]
        
        return None
   
   
    def getRowCount(self):
        return len(self.__data)
        
    
    def appendRow(self, data):
        r = len(self.__widgets)+1
        c = 0
        dataIdx = 0
        actualRow = []
        
        for columnData in data:
            widget = None
            if r > 1 and c == 0:
                widget = Button(self.__widgetFrame, text=columnData,
                                width=World.smallButtonWidth(),
                                command= lambda: self.__editRow(data))
            else:
                if dataIdx not in self.__invisibleColumns:
                    widget = Label(self.__widgetFrame, text=columnData)
                    
            if widget != None:                
                widget.grid(row=r, column=c,
                            padx=World.smallPadSize(), pady=World.smallPadSize())
                actualRow.append(widget)
                c += 1
                
            dataIdx += 1
            
        self.__widgets.append(actualRow)
        print("length of wiget container: " + str(len(self.__widgets)))
        self.__data.append(data)
    
    
    def getData(self, row, column):
        return self.__data[row][column]
    
    
    def getRowData(self, row):
        return self.__data[row]
    
    
    def getAllData(self):
        return self.__data
    
    
    def setRowData(self, row, data):
        self.__data[row] = data
        dataIdx = 0
        colIdx = 0
        for dataIdx in range(0, len(data)):
            if dataIdx not in self.__invisibleColumns:
                rowIdx = 0
                for actualRow in self.__widgets:
                    if rowIdx == row:
                        actualRow[colIdx].config(text=data[dataIdx])
                        break
                    rowIdx += 1
                colIdx += 1
        

        
    def setInvisibleColumns(self, columns):
        self.__invisibleColumns = columns
        
    
    def setState(self, state='disabled'):
        World.LOG().info("MinuxTable.setState called ")
        self.__plusButton.configure(state=state)
        for row in self.__widgets:
            for widget in row:
                if widget != None and widget.winfo_class() == 'Button':
                    widget.configure(state=state)
        
