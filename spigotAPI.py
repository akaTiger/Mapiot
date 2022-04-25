import lib
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class spigotTracker(object):
    def __init__(self, mainDisplay):
        self._main = mainDisplay
        self.funcName = "Spigot API Tracker"
        self._head = "https://api.spigotmc.org/simple/0.2/index.php"
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
    
    def query(self):
        choice = self._funcChoice.get()
        if self._funcLib[0][0] == choice:
            get = self._disbox.get("1.0", "end")
            get = get[:-1]
            if len(get) > 0:
                try:
                    l = get.split(",")
                    if len(l) == 1:
                        suf = "&category=" + str(l[0])
                        self.api(self._head + "?action=" + self._funcLib[0][1] + suf)
                    elif len(l) == 2:
                        suf = "&category=" + str(l[0]) + "&page=" + str(l[1])
                        self.api(self._head + "?action=" + self._funcLib[0][1] + suf)
                    else:
                        raise ValueError
                except:
                    self.api(self._head + "?action=" + self._funcLib[0][1])
            else:
                self.api(self._head + "?action=" + self._funcLib[0][1])
        
        elif self._funcLib[1][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[1][1])
        
        
        elif self._funcLib[2][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[2][1])
        
        
        elif self._funcLib[3][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[3][1])
        
        
        elif self._funcLib[4][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[4][1])
        
        
        elif self._funcLib[5][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[5][1])
        
        
        elif self._funcLib[6][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[6][1])
        
        
        elif self._funcLib[7][0] == choice:
            self.api(self._head + "?action=" + self._funcLib[7][1])
    
    def api(self, url):
        if True:
            self._disbox.delete("1.0", "end")
            self._disbox.insert(INSERT, url)
        