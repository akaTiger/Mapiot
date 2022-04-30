from tkinter.scrolledtext import ScrolledText
from turtle import width
from tkinter import *
import datetime
from slimeClasses import *

class slimeChunkDisplay(object):
    def __init__(self, mainDisplay):
        self.mainDisplay = mainDisplay
        self.fucSlimeChecker()
    
    def startSlimeChecker(self):
        starttime = datetime.datetime.now()
        startString = "+---++---++---+\n|NW || N || NE|\n+---++---++---+\n+---++---++---+\n| W || X || E |\n+---++---++---+\n+---++---++---+\n|SW || S || SE|\n+---++---++---+\n"
        self.scdInfoA.configure(bg="#FFAA55")
        self.scdInfoB.configure(bg="#FFAA55")
        self.scdInfoC.configure(bg="#FFAA55")
        self.scdInfoD.configure(bg="#FFAA55")
        self.scdInfoE.configure(bg="#FFAA55")
        self.scdInfoF.configure(bg="#FFAA55")
        self.scdInfoG.configure(bg="#FFAA55")
        self.scdInfoH.configure(bg="#FFAA55")
        self.scdInfoI.configure(bg="#FFAA55")
        
        def doTheJob(gameSeed, xPosition, zPosition):
            self.slimeChecker.setArgu(gameSeed, xPosition, zPosition)
            tupleR = self.slimeChecker.doCheck()
            return tupleR[0], tupleR
        
        gameSeed = int(self.gameSeed.get())
        xPosition = int(self.xPosition.get())
        zPosition = int(self.zPosition.get())
        
        cord = {
            "NW": [xPosition-1, zPosition+1],
            "N": [xPosition, zPosition+1],
            "NE": [xPosition+1, zPosition+1],
            "W": [xPosition-1, zPosition],
            "X": [xPosition, zPosition],
            "E": [xPosition+1, zPosition],
            "SW": [xPosition-1, zPosition-1],
            "S": [xPosition, zPosition-1],
            "SE": [xPosition+1, zPosition-1]
        }
        result = {
            "NW": None,
            "N": None,
            "NE": None,
            "W": None,
            "X": None,
            "E": None,
            "SW": None,
            "S": None,
            "SE": None
        }
        
        for way, cdn in cord.items():
            result[way] = doTheJob(gameSeed, cdn[0], cdn[1])[1][0]
        
        alg1 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][1])
        alg2 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][2])
        alg3 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][3])
        alg4 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][4])
        seedJava = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][5])
        
        endtime = datetime.datetime.now()
        
        if result["NW"] is True:
            self.scdInfoA.configure(bg="#A3FF55")
        if result["N"] is True:
            self.scdInfoB.configure(bg="#A3FF55")
        if result["NE"] is True:
            self.scdInfoC.configure(bg="#A3FF55")
        if result["W"] is True:
            self.scdInfoD.configure(bg="#A3FF55")
        if result["X"] is True:
            self.scdInfoE.configure(bg="#A3FF55")
        if result["E"] is True:
            self.scdInfoF.configure(bg="#A3FF55")
        if result["SW"] is True:
            self.scdInfoG.configure(bg="#A3FF55")
        if result["S"] is True:
            self.scdInfoH.configure(bg="#A3FF55")
        if result["SE"] is True:
            self.scdInfoI.configure(bg="#A3FF55")
        if True:
            self.scdListbox.delete("1.0", "end")
            self.scdListbox.insert(INSERT, startString)
            self.scdListbox.insert(INSERT, "\n")
            self.scdListbox.insert(INSERT, f"- Slime Chunks Report:\n")
            for way, rst in result.items():
                if len(way) == 1:
                    self.scdListbox.insert(INSERT, f"  | {way}  ----> {rst}\n")
                else:
                    self.scdListbox.insert(INSERT, f"  | {way} ----> {rst}\n")
            self.scdListbox.insert(INSERT, f"- More Info:\n")
            self.scdListbox.insert(INSERT, f"  | Seed:\n")
            self.scdListbox.insert(INSERT, f"  | | Game Seed: \n  | | {gameSeed}\n")
            self.scdListbox.insert(INSERT, f"  | | Java RNG Seed: \n  | | {seedJava}\n")
            self.scdListbox.insert(INSERT, f"  | Location:\n")
            self.scdListbox.insert(INSERT, f"  | | Chunk Cord X: {xPosition}\n")
            self.scdListbox.insert(INSERT, f"  | | Chunk Cord Z: {zPosition}\n")
            self.scdListbox.insert(INSERT, f"  | Version: Java Edition\n")
            self.scdListbox.insert(INSERT, f"  | Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            self.scdListbox.insert(INSERT, f"  | Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
            self.scdListbox.insert(INSERT, f"  | Process Time: {(endtime - starttime).microseconds} microseconds\n")
            self.scdListbox.insert(INSERT, f"  | Algorithm:\n")
            self.scdListbox.insert(INSERT, f"  | | x*x*0x4c1906: \n  | | {alg1}\n")
            self.scdListbox.insert(INSERT, f"  | | x*0x5ac0db: \n  | | {alg2}\n")
            self.scdListbox.insert(INSERT, f"  | | (z*z)*0x4307a7L: \n  | | {alg3}\n")
            self.scdListbox.insert(INSERT, f"  | | (z*0x5f24f)*0x3ad8025fL: \n  | | {alg4}\n")
    
    def fucSlimeChecker(self):
        if True:
            self.slimeChecker = slimeChecker()
            self.slimeCheckerDisplay = Frame(self.mainDisplay)
        
        if True:
            self.scdInfoFrame = Frame(self.slimeCheckerDisplay)
            self.scdInfoFrame.pack(fill="both", expand="yes")
        
        if True:
            self.scdInfoFrameL = Frame(self.scdInfoFrame)
            self.scdInfoFrameR = Frame(self.scdInfoFrame)
            self.scdInfoFrameL.pack(side="left")
            self.scdInfoFrameR.pack(side="left")
        
        if True:
            self.scdInfoA = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoB = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoC = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoD = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoE = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoF = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoG = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoH = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoI = Frame(self.scdInfoFrameL, bg="#FFAA55", width=100, height=100, borderwidth=2, relief="solid")
            self.scdInfoA.grid(row=0, column=0)
            self.scdInfoB.grid(row=0, column=1)
            self.scdInfoC.grid(row=0, column=2)
            self.scdInfoD.grid(row=1, column=0)
            self.scdInfoE.grid(row=1, column=1)
            self.scdInfoF.grid(row=1, column=2)
            self.scdInfoG.grid(row=2, column=0)
            self.scdInfoH.grid(row=2, column=1)
            self.scdInfoI.grid(row=2, column=2)
        
        if True:
            self.scdListbox = ScrolledText(self.scdInfoFrameR)
            self.scdListbox.pack(fill="both")
        
        if True:
            self.scdLabelFrame = LabelFrame(self.slimeCheckerDisplay, text="Arguments", padx=20, pady=10)
            self.gameSeed = Entry(self.scdLabelFrame, width=60)
            self.cordFrame = Frame(self.scdLabelFrame)
            self.xPosition = Entry(self.cordFrame, width=27)
            self.zPosition = Entry(self.cordFrame, width=27)
            self.scdStartButton = Button(self.scdLabelFrame, text="Search", width=20, command=self.startSlimeChecker)
        
        if True:
            self.slimeCheckerDisplay.pack(fill="both", expand="yes")
            self.scdLabelFrame.pack(fill="x", padx=20, pady=20, anchor="s")
            self.gameSeed.pack()
            self.gameSeed.insert(0, "-9050415789436934359")
            self.cordFrame.pack()
            self.xPosition.pack(side="left")
            self.xPosition.insert(0, "33")
            self.zPosition.pack(side="left")
            self.zPosition.insert(0, "-33")
            self.scdStartButton.pack()