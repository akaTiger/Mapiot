from tkinter.scrolledtext import ScrolledText
from turtle import width
import requests
import json
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from bs4 import BeautifulSoup
from tkinter import *
import io
import datetime

class app(object):
    def __init__(self, projName, windowWidth, windowLength):
        self.projName = projName
        self.windowWidth = windowWidth
        self.windowLength = windowLength
        self.root = Tk()
        self.windowConfigure()
        self.mainFrameInit()
        self.fucSlimeChecker()
        self.root.mainloop()
        
        
    def windowConfigure(self):
        self.root.title(self.projName)
        self.root.update_idletasks()
        width = 900
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        height = 850
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()
        self.root.resizable(False, False)
        self.root.update()
    
    def mainFrameInit(self):
        self.topMenu = Frame(self.root, height=30, background="green")
        self.mainDisplay = Frame(self.root, background="blue")
        self.topMenu.pack(fill="x", anchor="n")
        self.mainDisplay.pack(fill="both", expand="yes", anchor="n")
    
    def clearMainDisplay(self):
        for i in self.mainDisplay.winfo_children():
            i.destroy()
    
    def startSlimeChecker(self):
        starttime = datetime.datetime.now()
        startString = "+++++++++++++++\n|NW || N || NE|\n+++++++++++++++\n+++++++++++++++\n| W || X || E |\n+++++++++++++++\n+++++++++++++++\n|SW || S || SE|\n+++++++++++++++\n"
        def doTheJob(gameSeed, xPosition, zPosition):
            self.slimeChecker.setArgu(gameSeed, xPosition, zPosition)
            tupleR = self.slimeChecker.doCheck()
            return tupleR[0], tupleR
        gameSeed = int(self.gameSeed.get())
        xPosition = int(self.xPosition.get())
        zPosition = int(self.zPosition.get())
        
        cord = {
            "NW": [xPosition - 1, zPosition + 1],
            "N": [xPosition, zPosition + 1],
            "NE": [xPosition + 1, zPosition + 1],
            "W": [xPosition - 1, zPosition],
            "X": [xPosition, zPosition],
            "E": [xPosition + 1, zPosition],
            "SW": [xPosition - 1, zPosition - 1],
            "S": [xPosition, zPosition - 1],
            "SE": [xPosition + 1, zPosition - 1]
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
            result[way] = str(doTheJob(gameSeed, cdn[0], cdn[1])[1][0])
        
        alg1 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][1])
        alg2 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][2])
        alg3 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][3])
        alg4 = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][4])
        seedJava = str(doTheJob(gameSeed, cord["X"][0], cord["X"][1])[1][5])
        
        endtime = datetime.datetime.now()
        
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
        self.scdListbox.insert(INSERT, f"  | | Game Seed: {gameSeed}\n")
        self.scdListbox.insert(INSERT, f"  | | Java RNG Seed: {seedJava}\n")
        self.scdListbox.insert(INSERT, f"  | Location:\n")
        self.scdListbox.insert(INSERT, f"  | | Chunk Cord X: {xPosition}\n")
        self.scdListbox.insert(INSERT, f"  | | Chunk Cord Z: {zPosition}\n")
        self.scdListbox.insert(INSERT, f"  | Version: Java Edition\n")
        self.scdListbox.insert(INSERT, f"  | Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
        self.scdListbox.insert(INSERT, f"  | Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
        self.scdListbox.insert(INSERT, f"  | Process Time: {(endtime - starttime).microseconds} microseconds\n")
        self.scdListbox.insert(INSERT, f"  | Algorithm:\n")
        self.scdListbox.insert(INSERT, f"  | | x*x*0x4c1906: {alg1}\n")
        self.scdListbox.insert(INSERT, f"  | | x*0x5ac0db: {alg2}\n")
        self.scdListbox.insert(INSERT, f"  | | (z*z)*0x4307a7L: {alg3}\n")
        self.scdListbox.insert(INSERT, f"  | | (z*0x5f24f)*0x3ad8025fL: {alg4}\n")
        
        
    
    def fucSlimeChecker(self):
        self.clearMainDisplay()
        self.slimeChecker = slimeChecker()
        self.slimeCheckerDisplay = Frame(self.mainDisplay)
        
        self.isNotSlime = StringVar()
        self.isNotSlime.set("input arguments to start")
        
        self.scdInfoFrame = Frame(self.slimeCheckerDisplay)
        self.scdInfoFrame.pack(fill="both", expand="yes")
        self.scdListbox = ScrolledText(self.scdInfoFrame, font=("Courier", 30), width=60, height=20)
        self.scdListbox.pack()
        
        self.scdLabel = Label(self.slimeCheckerDisplay, textvariable=self.isNotSlime)
        self.scdLabelFrame = LabelFrame(self.slimeCheckerDisplay, text="Arguments", padx=20, pady=10)
        self.gameSeed = Entry(self.scdLabelFrame, width=50)
        self.xPosition = Entry(self.scdLabelFrame, width=10)
        self.zPosition = Entry(self.scdLabelFrame, width=10)
        self.scdStartButton = Button(self.scdLabelFrame, text="Search", width=20, command=self.startSlimeChecker)
        
        
        
        self.slimeCheckerDisplay.pack(fill="both", expand="yes")
        self.scdLabel.pack()
        self.scdLabelFrame.pack(fill="x", padx=20, pady=20, anchor="s")
        self.gameSeed.pack(side="left")
        self.gameSeed.insert(0, "-9050415789436934359")
        self.xPosition.pack(side="left")
        self.xPosition.insert(0, "33")
        self.zPosition.pack(side="left")
        self.zPosition.insert(0, "-33")
        self.scdStartButton.pack(side="left")
        
    

class slimeChecker(object):
    def __init__(self):
        self.gameSeed = None
        self.xPosition = None
        self.zPosition = None
    def setArgu(self, gameSeed, xPosition, zPosition):
        self.gameSeed = gameSeed
        self.xPosition =  xPosition
        self.zPosition = zPosition
    def int_overflow(self, val, maxint):
        if not -maxint-1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val
    @property
    def seed(self):
        return self._seed
    @seed.setter
    def seed(self, seed):
        self._seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1)
    def next(self, bits):
        if bits < 1:
            bits = 1
        elif bits > 32:
            bits = 32
        self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) - 1)
        retval = self._seed >> (48 - bits)
        if retval & (1 << 31):
            retval -= (1 << 32)
        return retval
    def javaRandomNextInt(self, n=None):
        if not (n & (n - 1)):
            return (n * self.next(31)) >> 31
        bits = self.next(31)
        val = bits % n
        while (bits - val + n - 1) < 0:
            bits = self.next(31)
            val = bits % n
        return val
    def doCheck(self):
        if (self.gameSeed == None) or (self.xPosition == None) or (self.zPosition == None):
            raise ValueError("set seed, xPosition, zPosition first!")
        else:
            javaIntLimit = 2147483647
            javaLongLimit = 9223372036854775807
            mcAlgorA = self.int_overflow(self.int_overflow(self.xPosition * self.xPosition * 0x4c1906, javaIntLimit), javaLongLimit)
            mcAlgorB = self.int_overflow(self.int_overflow(self.xPosition * 0x5ac0db, javaIntLimit), javaLongLimit)
            mcAlgorC = self.int_overflow((self.int_overflow(self.zPosition * self.zPosition, javaIntLimit) * 0x4307a7), javaLongLimit)
            mcAlgorD = self.int_overflow((self.int_overflow(self.zPosition * 0x5f24f, javaIntLimit)), javaLongLimit)
            self.seed = (self.int_overflow(((self.gameSeed + mcAlgorA + mcAlgorB + mcAlgorC + mcAlgorD )^ 0x3ad8025f), javaLongLimit))
            return str(self.javaRandomNextInt(10) == 0), str(mcAlgorA), str(mcAlgorB), str(mcAlgorC), str(mcAlgorD), str(self.seed)

if __name__ == "__main__":
    startScript = app("Mapiot", 900, 850)