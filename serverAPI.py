from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests
import json
import base64
import io
from PIL import Image, ImageTk
import struct


class serverAPI(object):
    def __init__(self, mainDisplay):
        self.main = mainDisplay
        self.initFrame()
    # def __init__(self):
    #     pass
    
    def cstb(self, string):
        bytes = b''
        for i in string:
            bytes += struct.pack("B", ord(i))
        return bytes
    
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
            self.ip = Entry(self.query)
            self.ip.pack(side="left", fill="x", expand="yes")
            self.ip.insert(0, "play.hypixel.net")
            Button(self.query, text="Search", command=self.api).pack(side="left")
    
    # find targets
    def infoA(self):
        self.cinfo["Server Ip"] = self.js["ip"]
    def infoB(self):
        self.cinfo["Port"] = self.js["port"]
    def infoC(self):
        self.cinfo["Ping"] = self.js["debug"]["ping"]
    def infoD(self):
        self.cinfo["Server Default Query"] = self.js["debug"]["query"]
    def infoE(self):
        self.cinfo["IP SRV"] = self.js["debug"]["srv"]
    def infoF(self):
        self.cinfo["Query Mismatch"] = self.js["debug"]["querymismatch"]
    def infoG(self):
        self.cinfo["IP in SRV"] = self.js["debug"]["ipinsrv"]
    def infoH(self):
        self.cinfo["CNAME in SRV"] = self.js["debug"]["cnameinsrv"]
    def infoI(self):
        self.cinfo["Animated Motd"] = self.js["debug"]["animatedmotd"]
    def infoJ(self):
        self.cinfo["Cache Time"] = self.js["debug"]["cachetime"]
    def infoK(self):
        self.cinfo["API Version"] = self.js["debug"]["apiversion"]
    def infoL(self):
        zro = 0
        for i in self.js["motd"]["clean"]:
            self.cinfo["Motd Line " + str(zro)] = i.strip()
            zro += 1
    def infoM(self):
        self.cinfo["Players Stats"] = f'{self.js["players"]["online"]} / {self.js["players"]["max"]}'
    def infoN(self):
        self.cinfo["Version on Motd"] = self.js["version"]
    def infoO(self):
        self.cinfo["Online Server"] = self.js["online"]
    def infoP(self):
        self.cinfo["Protocol"] = self.js["protocol"]
    def infoQ(self):
        self.cinfo["Host Name"] = self.js["hostname"]
    def infoR(self):
        self.rawicon = self.js["icon"]
    def infoS(self):
        for key, val in self.js["players"]["uuid"].items():
            self.plst[key] = val
    
    def infoGet(self, ip):
        url = "https://api.mcsrvstat.us/2/" + ip
        js = json.dumps(json.loads(requests.get(url).text))
        self.js = json.loads(js)
        self.cinfo = {}
        self.plst = {}
        processlst = [
            self.infoA,
            self.infoB,
            self.infoC,
            self.infoD,
            self.infoE,
            self.infoF,
            self.infoG,
            self.infoH,
            self.infoI,
            self.infoJ,
            self.infoK,
            self.infoL,
            self.infoM,
            self.infoN,
            self.infoO,
            self.infoP,
            self.infoQ,
            self.infoR,
            self.infoS
        ]
        # process funclst
        for i in processlst:
            try:
                i()
            except:
                pass
        return self.cinfo, self.rawicon, self.plst
    
    # ava to imagetk 10,10 size
    def getAva(self, uuid):
        url = "https://crafatar.com/avatars/" + uuid
        image = ImageTk.PhotoImage(Image.open(io.BytesIO(requests.get(url).content)).resize((10, 10)))
        self.images.append(image)
        self.comp.image_create(INSERT, padx=5, pady=5, image=self.images[-1])
    
    # main func  
    def api(self):
        # ava keep reference
        self.images = []
        if True:
            # usr input get
            ip = self.ip.get()
        if True:
            # clear left and right
            for i in self.left.winfo_children():
                i.destroy()
            for i in self.right.winfo_children():
                i.destroy()
        if True:
            # get picture
            infortn = self.infoGet(ip)
            self.basicDic = infortn[0]
            bpic = self.cstb(infortn[1][22:])
            picIO = io.BytesIO(base64.b64decode(bpic))
        if True:
            # picture label
            img = ImageTk.PhotoImage(Image.open(picIO).resize((190, 190)))
            self.pl = Label(self.left, image=img)
            self.pl.image = img
            self.pl.pack(padx=20, pady=20)
        if True:
            # basic info
            self.basic = ScrolledText(self.left, width=25, height=10)
            self.basic.pack(padx=20, pady=20)
            self.basic.insert(INSERT, "|>>>>>--- INFO ---<<<<\n")
            for key, val in self.basicDic.items():
                self.basic.insert(INSERT, f"|-> {key}:\n|{val}\n")
        if True:
            # player info
            self.comp = ScrolledText(self.right)
            self.comp.pack(padx=20, pady=20, fill="both", expand="yes")
            self.comp.insert(INSERT, f"|>>>>>--- Players (If avaliable) ---<<<<\n")
            for key, val in infortn[2].items():
                self.comp.insert(INSERT, f"|-> ")
                self.getAva(val)
                self.comp.insert(INSERT, f"ID: {key}\n|   {val}\n")