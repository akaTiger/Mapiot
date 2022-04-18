from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import io
import requests
from mojang import MojangAPI
import datetime

class playerAPI(object):
    def __init__(self, mainDisplay):
        self.main = mainDisplay
        self.initFrame()
    
    def infoInsert(self, id):
        
        uuid = MojangAPI.get_uuid(id)
        prof = MojangAPI.get_profile(uuid)
        skin = prof.skin_url
        nameHis = MojangAPI.get_name_history(uuid)
        self.endtime = datetime.datetime.now()

        self.basic.insert(INSERT, f"Username: \n{id}\n")
        self.basic.insert(INSERT, f"\nProcess Time: \n{(self.endtime-self.starttime).microseconds / 1000} ms\n")
        self.comp.insert(INSERT, f"UUID: \n{uuid}\n")
        self.comp.insert(INSERT, f"\nSkin URL: \n{skin}\n")
        self.comp.insert(INSERT, f"\nName History: \n")
        for i in nameHis:
            if i['changed_to_at'] == 0:
                self.comp.insert(INSERT, f"{i['name']} was the user's first name\n")
            else:
                self.comp.insert(INSERT, f"{i['name']} on {datetime.datetime.fromtimestamp(i['changed_to_at'] / 1000, datetime.timezone.utc)}\n")
        self.comp.insert(INSERT, "\nSkull Cmd 1.13+: \n/give @s minecraft:player_head{SkullOwner:'"+ str(id) +"'}\n")
        self.comp.insert(INSERT, '\nSkull Cmd 1.12: \n/give @p minecraft:skull 1 3 {SkullOwner:"'+ str(id) +'"}\n')
        self.comp.insert(INSERT, '\nChange Head Cmd: \n/replaceitem entity @p slot.armor.head minecraft:skull 1 3 {SkullOwner:"' + str(id) + '"}')
        
    def api(self):
        self.starttime = datetime.datetime.now()
        for i in self.left.winfo_children():
            i.destroy()
        for i in self.right.winfo_children():
            i.destroy()
        opt = self.optVar.get()
        val = self.id.get()
        if opt == "ID":
            if True:
                url = str("https://minotar.net/armor/bust/" + val + "/190.png")
                image = ImageTk.PhotoImage(Image.open(io.BytesIO(requests.get(url).content)))
                self.avat = Label(self.left, image=image, borderwidth=2, relief="solid")
                self.avat.image = image
                self.avat.pack(padx=20, pady=20)
            if True:
                self.basic = ScrolledText(self.left, width=25, height=10)
                self.basic.pack(padx=20, pady=10)
                
                self.comp = ScrolledText(self.right)
                self.comp.pack(padx=20, pady=20, fill="both", expand="yes")
                
                self.infoInsert(val)
                
    
    def initFrame(self):
        if True:
            self.info = Frame(self.main)
            self.input = Frame(self.main, height=150)
            self.info.pack(fill="both", expand="yes")
            self.input.pack(fill="x")
            self.left = Frame(self.info)
            self.right = Frame(self.info)
            self.left.pack(side="left", fill="y")
            self.right.pack(side="left", fill="both", expand="yes")
            self.query = LabelFrame(self.input, text="Query Input", padx=10, pady=10)
            self.query.pack(fill="both", padx=10, pady=10)
        if True:
            self.optVar = StringVar()
            self.optVar.set("ID")
            self.opt = [
                "ID"
            ]
            OptionMenu(self.query, self.optVar, *self.opt).pack(side="left")
            self.id = Entry(self.query)
            self.id.pack(side="left", fill="x", expand="yes")
            self.id.insert(0, "LilT1ger")
            Button(self.query, text="Search", command=self.api).pack(side="left")