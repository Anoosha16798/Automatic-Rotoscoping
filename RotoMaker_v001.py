import FindMattes as fm
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
from os import listdir
import os
from pathlib import Path
#fm.createMatte("/Users/amithannigeri/Desktop/python-codes/AutoRoto01/ManyCycle.png","/Users/amithannigeri/Desktop/python-codes/AutoRoto01/ManyCycle_matte.png",256)


# Get the file directory
root = tk.Tk()
root.withdraw()
directoryName = filedialog.askdirectory(parent=root,initialdir="/",title = 'Please select a directory')
matteHeight = sd.askinteger("Set the matte size","Output matte vertical resolution( 256 recommended for quick test)?",parent=root,initialvalue=256)
#print("User picked" + str(matteHeight))
listOfFiles = listdir(directoryName)

def abc(n):
        for abc in n:
                f= abc.find("_matte")
                print(f)
                if f != -1:
                        n.remove(abc)
                print(abc)
                print('job done')

abc(listOfFiles)

for currentFile in listOfFiles: 
    #findfile = currentFile.find('_matte')
    #del findfile    
        print("Current file: " + currentFile)
        sourceFile=directoryName+ "/" + currentFile
        print("Current file(full Path) : " + sourceFile)
        mainNameEnd = currentFile.find('.')
        nameForMatte=currentFile[:mainNameEnd]+ "_matte" +currentFile[mainNameEnd:]
        fullPathMatteName=directoryName+ "/" + nameForMatte
        fm.createMatte(sourceFile, fullPathMatteName, matteHeight)
        print("just created: "+ nameForMatte)
    
    
    