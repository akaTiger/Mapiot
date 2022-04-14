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
        gameSeed = int(self.gameSeed.get())
        xPosition = int(self.xPosition.get())
        zPosition = int(self.zPosition.get())
        self.slimeChecker.setArgu(gameSeed, xPosition, zPosition)
        self.isNotSlime.set(str(self.slimeChecker.doCheck()))
    
    def fucSlimeChecker(self):
        self.clearMainDisplay()
        self.slimeChecker = slimeChecker()
        self.slimeCheckerDisplay = Frame(self.mainDisplay)
        self.isNotSlime = StringVar()
        self.isNotSlime.set("input arguments to start")
        self.scdLabel = Label(self.slimeCheckerDisplay, textvariable=self.isNotSlime)
        self.scdLabelFrame = LabelFrame(self.slimeCheckerDisplay, text="Arguments", padx=10, pady=10)
        self.gameSeed = Entry(self.scdLabelFrame)
        self.xPosition = Entry(self.scdLabelFrame)
        self.zPosition = Entry(self.scdLabelFrame)
        self.scdStartButton = Button(self.scdLabelFrame, text="Search", command=self.startSlimeChecker)
        
        
        
        self.slimeCheckerDisplay.pack(fill="both", expand="yes")
        self.scdLabel.pack()
        self.scdLabelFrame.pack()
        self.gameSeed.pack()
        self.gameSeed.insert(0, "-9050415789436934359")
        self.xPosition.pack()
        self.xPosition.insert(0, "33")
        self.zPosition.pack()
        self.zPosition.insert(0, "-33")
        self.scdStartButton.pack()
        
    

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
            return self.javaRandomNextInt(10) == 0

if __name__ == "__main__":
    startScript = app("Mapiot", 900, 850)