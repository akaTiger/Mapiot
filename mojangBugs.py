from tkinter import *
from tkinter.scrolledtext import ScrolledText
import lib
from browser import *
from bs4 import BeautifulSoup


class mojBug(object):
    def __init__(self, mainDisplay):
        self.main = mainDisplay
        self._funcName = "Mojang Open Issues Checker"
        self._head = lib.getMojangUrlHead()
        self._debugFile = lib.getDebugFile()
        self._versions = lib.getVersion()
        self._projects = lib.getProject()
        self._stats = lib.getStatus()
        
        self.initFrame()
    
    def debug(self, a):
        with open(self._debugFile, "w") as file:
            file.write(str(a))
    
    def initFrame(self):
        if True:
            # info Frame
            self.info = Frame(self.main)
            self.info.pack(fill="both", expand="yes")
            
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
            self._project.set("MC")
            self._stat.set("Open")
        
        if True:
            # self.query frames
            frameTop = Frame(self.query)
            frameBot = Frame(self.query)
            frameTop.pack(expand="yes", fill="x")
            frameBot.pack(expand="yes", fill="x")
        
        if True:
            # scroll text
            self._disbox = ScrolledText(self.info)
            self._disbox.pack(fill="both", expand="yes", padx=10, pady=10)
        
        if True:
            # options widget
            OptionMenu(frameTop, self._project, *self._projects).pack(side="left", expand="yes", fill="x")
            OptionMenu(frameTop, self._version, *self._versions).pack(side="left", expand="yes", fill="x")
            OptionMenu(frameTop, self._stat, *self._stats).pack(side="left", expand="yes", fill="x")
            self._entry = Entry(frameBot)
            self._entry.pack(side="left", expand="yes", fill="x")
            Button(frameBot, text="Apply & Search", command=self.api).pack(side="left")

    def jqStr(self, lst):
        # lst [project, status, version, text]
        dic = lib.getUrlSymbol()
        
        if True:
            # format
            jqAttr = []
            for i in lst[:-1]:
                if " " in i:
                    jqAttr.append(str('"') + i + str('"'))
                else:
                    jqAttr.append(i)
            jqAttr.append(str('"') + lst[-1] + str('"'))
            
        if True:
            # url pre gen
            if jqAttr[3] == "":
                jq = f"project = {jqAttr[0]} AND status = {jqAttr[1]} AND affectedVersion = {jqAttr[2]} ORDER BY votes DESC, updated DESC"
            else:
                jq = f"project = {jqAttr[0]} AND status = {jqAttr[1]} AND affectedVersion = {jqAttr[2]} AND text ~ {jqAttr[3]} ORDER BY votes DESC, updated DESC"
        
        if True:
            # url gen
            url = []
            for i in jq:
                if i in dic.keys():
                    url.append(dic[i])
                else:
                    url.append(i)
            return "".join(url)

    def api(self):
        if True:
            # info pre
            infoGet = [self._project.get(), self._stat.get(), self._version.get(), self._entry.get()]
            # info pull from target
            jqKeys = self.jqStr(infoGet)
            fullurl = self._head + jqKeys
            c = 'issue-list'
            html = webD(fullurl, c)
        
        if True:
            # html filter
            bs = BeautifulSoup(html, features="lxml")
            self.raw = bs.find_all('li')
        
        if True:
            # text out
            pre = []
            for i in self.raw:
                pre.append(f"[{i.get('data-key')}] \t{i.get('title')}\n")
            self._disbox.delete("1.0", "end")
            for i in pre:
                self._disbox.insert(INSERT, i)
        
        