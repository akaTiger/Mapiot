from tkinter import *
from slimeChunkDisplay import *
from playerAPI import *
from serverAPI import *
from mojangBugs import *
from spigotAPI import *

class app(object):
    def __init__(self, projName, windowWidth, windowLength):
        self.projName = projName
        self.windowWidth = windowWidth
        self.windowLength = windowLength
        self.root = Tk()
        self.windowConfigure()
        self.mainFrameInit()
        self.topMenuDisplay()
        # self.fucSlimeChecker()
        self.root.update()
        self.root.mainloop()
        
    def windowConfigure(self):
        self.root.title(self.projName)
        self.root.update_idletasks()
        width = self.windowWidth
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        height = self.windowLength
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()
        self.root.resizable(False, False)
        self.root.update()
    
    def mainFrameInit(self):
        self.topMenu = Frame(self.root, height=30)
        self.mainDisplay = Frame(self.root)
        self.topMenu.pack(fill="x", anchor="n")
        self.mainDisplay.pack(fill="both", expand="yes", anchor="n")
    
    def clearMainDisplay(self):
        for i in self.mainDisplay.winfo_children():
            i.destroy()
    
    def topMenuDisplay(self):
        self.tmdFuncOptions = [
            "Java Edition Slime Chunks Checker",
            "Player API Query",
            "Server API Query",
            "Mojang Open Issues Checker",
            "Spigot Resource Update Tracker"
        ]
        self.tmdFuncVar = StringVar()
        self.tmdFuncVar.set("Player API Query")
        self.tmdOptionMenu = OptionMenu(self.topMenu, self.tmdFuncVar, *self.tmdFuncOptions)
        self.tmdOptionMenu.pack(fill="x", expand="yes", side="left")
        self.tmdFuncSelectButton = Button(self.topMenu, text="Go", command=self.startSelectedFunc)
        self.tmdFuncSelectButton.pack(side="left", anchor="e")
    
    def startSelectedFunc(self):
            selectedValue = self.tmdFuncVar.get()
            if selectedValue == self.tmdFuncOptions[0]:
                self.clearMainDisplay()
                self.fsc = slimeChunkDisplay(self.mainDisplay)
            elif selectedValue == self.tmdFuncOptions[1]:
                self.clearMainDisplay()
                self.papi = playerAPI(self.mainDisplay)
            elif selectedValue == self.tmdFuncOptions[2]:
                self.clearMainDisplay()
                self.sapi = serverAPI(self.mainDisplay)
            elif selectedValue == self.tmdFuncOptions[3]:
                self.clearMainDisplay()
                self.mojBug = mojBug(self.mainDisplay)
            elif selectedValue == self.tmdFuncOptions[4]:
                self.clearMainDisplay()
                self.spigot = spigotTracker(self.mainDisplay)

if __name__ == "__main__":
    startScript = app("Mapiot", 600, 520)
    # im lazy