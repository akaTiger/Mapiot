from tkinter import *
import lib
class mojBug(object):
    def __init__(self, mainDisplay):
        self.main = mainDisplay
        self._funcName = "Mojang Open Issues Checker"
        self.initFrame()
    def initFrame(self):
        if True:
            # info Frame
            self.info = Frame(self.main)
            self.info.pack(fill="both", expand="yes")
            # info left
            self.left = Frame(self.info)
            self.left.pack(side="left", fill="y")
            # info right
            self.right = Frame(self.info)
            self.right.pack(side="left", fill="both", expand="yes")
            
        if True:
            # input Frame
            self.input = Frame(self.main, height=150)
            self.input.pack(fill="x")
            # input block
            self.query = LabelFrame(self.input, text="Filters", padx=10, pady=10)
            self.query.pack(fill="both", padx=10, pady=10)
            
        if True:
            # init filter var
            self._version = StringVar()
            self._project = StringVar()
            self._stat = StringVar()
        
        if True:
            # init option menu
            self._version.set("EMPTY")
            self._versions = lib.version()
            self._project.set("MC")
            self._projects = lib.project()
            self._stat.set("Open")
            self._stats = lib.status()
        
        if True:
            frameTop = Frame(self.query)
            frameBot = Frame(self.query)
            frameTop.pack(expand="yes", fill="x")
            frameBot.pack(expand="yes", fill="x")
        if True:
            # options widget
            OptionMenu(frameTop, self._project, *self._projects).pack(side="left", expand="yes", fill="x")
            OptionMenu(frameTop, self._version, *self._versions).pack(side="left", expand="yes", fill="x")
            OptionMenu(frameTop, self._stat, *self._stats).pack(side="left", expand="yes", fill="x")
            Entry(frameBot).pack(side="left", expand="yes", fill="x")
            
        if True:
            Button(frameBot, text="Apply & Search", command=self.api).pack(side="left")
    def api(self):
        pass
    
    
    