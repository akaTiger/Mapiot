from tkinter import *
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
            self.query = LabelFrame(self.input, text="Query Input", padx=10, pady=10)
            self.query.pack(fill="both", padx=10, pady=10)
            
        if True:
            self.optVar = StringVar()
            self.optVar.set("Server IP")
            self.opt = [
                "Server IP"
            ]
            OptionMenu(self.query, self.optVar, *self.opt).pack(side="left")
            
            Button(self.query, text="Apply", command=self.api).pack(side="left")
    def api(self):
        pass
    
    
    