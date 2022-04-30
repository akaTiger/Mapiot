import lib
import errorClasses as er
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
from spigotClasses import *

class spigotTracker(object):
    def __init__(self, mainDisplay):
        self._main = mainDisplay
        self.funcName = "Spigot API Tracker"
        self._workDirectory = Path(__file__).parent
        self._errorMessage = lib.errorMessage()
        self._nameLib = [i[0] for i in lib.getParameters().values()]
        self._funcLib = lib.getParameters()
        self.initFrame()
    
    def initFrame(self):
        if True:
            # Upper
            self._displayFrame = Frame(self._main)
            self._displayFrame.pack(fill="both", expand="yes")
            
        if True:
            # input Frame
            self._inputFrame = Frame(self._main, height=150)
            self._inputFrame.pack(fill="x")
            # input block
            self._lF = LabelFrame(self._inputFrame, text="Filters", padx=10, pady=10)
            self._lF.pack(fill="both", padx=10, pady=10)
        
        if True:
            # scroll text
            self._disbox = ScrolledText(self._displayFrame)
            self._disbox.pack(fill="both", expand="yes", padx=10, pady=10)
        
        if True:
            self._funcChoice = StringVar()
        if True:
            # options widget
            OptionMenu(self._lF, self._funcChoice, *self._nameLib).pack(expand="yes", fill="x")
            Button(self._lF, text="Execute", command=self.query).pack(expand="yes", fill="x")
    
    def debug(self):
        print(self._funcChoice.get())
    
    def writeIn(self, info):
        if True:
            self._disbox.delete("1.0", "end")
            self._disbox.insert(INSERT, info)
    
    def query(self):
        apiObj = spigotAPI()
        choice = self._funcChoice.get()
        # get all
        if self._funcLib[0][0] == choice:
            try:
                write = apiObj.listResources(get=(self._disbox.get("1.0", "end"))[:-1])
                self.writeIn(info=write)
            except (er.parameterError, AssertionError):
                write = lib.errorMessage()
                self.writeIn(info=write["parameter"])
            except:
                write = lib.errorMessage()
                self.writeIn(info=write["unexpected"])
                
            
            
            
            
            
        
        # build a custom text changer txt file to change the language of the script, excecute in main.py
        