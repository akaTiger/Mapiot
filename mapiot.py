from bdb import Breakpoint
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
import tkinter as tk
import io

# Custom Exceptions Start
class invalidInputInfo(Exception):
    pass
class clearList(Exception):
    pass
# Custom Exceptions End
# ---------------
# Player API Start
def playerUUIDgui():
    homeUnpack()
    canvasFrame = tk.Frame(mapiot)
    canvasFrame.pack()
    def startThisFunc():
        try:
            for skinC in canvasFrame.winfo_children():
                skinC.destroy()
        except:
            pass
        uI = usrInput.get()
        try:
            getInfo = playerAPI(uI)
            outBlock.set(getInfo[0])
            # image size 552x736
            url = str("https://minecraftskinstealer.com/api/v1/skin/render/fullbody/" + getInfo[1] + "/700")
            skinVar.set(url)
            skinImage = ImageTk.PhotoImage(Image.open(io.BytesIO(requests.get(skinVar.get()).content)))
            skinCanvas = tk.Label(canvasFrame, image=skinImage, bg="white")
            skinCanvas.image = skinImage
            skinCanvas.pack()
            
        except invalidInputInfo:
            outBlock.set("Invalid Info")
    outBlock = tk.StringVar()
    skinVar = tk.StringVar()
    skinVar.set("https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png")
    # https://minecraftskinstealer.com/api/v1/skin/render/fullbody/LilT1ger/700
    # https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png
    
    outLable = tk.Label(mapiot, textvariable=outBlock, font=('Arial', 14))
    outLable.pack()
    usrInput = tk.Entry(mapiot, show=None, font=('Arial', 14))
    usrInput.pack()
    startIt = tk.Button(mapiot, text = 'Search', command=startThisFunc)
    startIt.pack()
    
    def fucExit():
        homePack()
        buttonExit.pack_forget()
        try:
            usrInput.pack_forget()
            startIt.pack_forget()
            outLable.pack_forget()
            canvasFrame.destroy()
        except:
            pass
    buttonExit = tk.Button(mapiot, text = 'Back to home', command=fucExit)
    buttonExit.pack()
def formatUUID(uuid):
    outLst = [alphabit for alphabit in uuid if alphabit != "-"]
    return "".join(outLst)
def testUUID(uuid):
    fullURL = "https://api.minetools.eu/profile/" + uuid
    content = requests.get(url=fullURL)
    result = json.loads(content.text)
    try:
        if str(result["decoded"]) == "None":
            return False
        else:
            return True
    except:
        return False
def playerAPI(infoIn):
    toolDict = {
            "MoJangAPI": "https://api.mojang.com/user/profiles/",
            # "MineToolsEU": "https://api.minetools.eu/profile/"
        }
    if testUUID(infoIn) is False:
        raise invalidInputInfo()
    for tool in toolDict.keys():
        if tool == "MoJangAPI":
            infoNeeded = formatUUID(infoIn)
            FullURL = toolDict[tool] + infoNeeded + "/names"
            content = requests.get(url=FullURL)
            nameLst = json.loads(content.text)
            if len(nameLst) > 1:
                infoA = nameLst[-1]["name"]
                previousName = []
                for name in nameLst[:-1]:
                    previousName.append(name["name"])
                infoB = "Used IDs: " + "; ".join(previousName)
            if len(nameLst) == 1:
                infoA = nameLst[0]["name"]
    returnLst = []
    returnLst.append(str("-=" * 15))
    returnLst.append(str("Current ID: " + infoA))
    returnLst.append(infoB)
    returnLst.append(str("-=" * 15))
    return "\n".join(returnLst), infoA
# Player API End
# ---------------
# Server API Start
def serverAPIgui():
    homeUnpack()
    def startThisFunc():
        uI = usrInputIP.get()
        uI2 = usrInputPort.get()
        try:
            outBlock.set(serverAPI(uI, uI2))
        except invalidInputInfo:
            outBlock.set("Invalid Info")
    outBlock = tk.StringVar()
    outBlock.set("Ip in upper box \nport in lower box \ntype 0 indicate default port")
    outLable = tk.Label(mapiot, textvariable=outBlock, font=('Arial', 14))
    outLable.pack()
    usrInputIP = tk.Entry(mapiot, show=None, font=('Arial', 14))
    usrInputIP.pack()
    usrInputPort = tk.Entry(mapiot, show=None, font=('Arial', 14))
    usrInputPort.pack()
    startIt = tk.Button(mapiot, text = 'Search', command=startThisFunc)
    startIt.pack()
    def fucExit():
        homePack()
        buttonExit.pack_forget()
        usrInputIP.pack_forget()
        usrInputPort.pack_forget()
        startIt.pack_forget()
        outLable.pack_forget()
    buttonExit = tk.Button(mapiot, text = 'Back to home', command=fucExit)
    buttonExit.pack()
def minecraftColorcodeTranslate(letter):
    mcFontDict = {
        "DARK_RED": ["\u00A74", "&4"],
        "RED": ["\u00A7c", "&c"],
        "GOLD": ["\u00A76", "&6"],
        "YELLOW": ["\u00A7e", "&e"],
        "DARK_GREEN": ["\u00A72", "&2"],
        "GREEN": ["\u00A7a", "&a"],
        "AQUA": ["\u00A7b", "&b"],
        "DARK_AQUA": ["\u00A73", "&3"],
        "DARK_BLUE": ["\u00A71", "&1"],
        "BLUE": ["\u00A79", "&9"],
        "LIGHT_PURPLE": ["\u00A7d", "&d"],
        "DARK_PURPLE": ["\u00A75", "&5"],
        "WHITE": ["\u00A7f", "&f"],
        "GRAY": ["\u00A77", "&7"],
        "DARK_GRAY": ["\u00A78", "&8"],
        "BLACK": ["\u00A70", "&0"],
        "FONT_RESET": ["\u00A7r", "&r"],
        "FONT_BOLD": ["\u00A7l", "&l"],
        "FONT_ITALIC": ["\u00A7o", "&o"],
        "FONT_UNDERLINE": ["\u00A7n", "&n"],
        "FONT_STRIKE": ["\u00A7m", "&m"]
    }
    for colorCodes in mcFontDict.keys():
        letter = letter.replace(mcFontDict[colorCodes][0], mcFontDict[colorCodes][1])
    letter = letter.replace("&gt;&gt;&gt;", ">>>")
    return letter
def serverAPI(infoIn, gamePort):
    toolDict = {
        "mcsrvstat": "https://api.mcsrvstat.us/2/",
        "mcapi": "https://mcapi.us/server/status?ip=",
    }
    dumpLst = []
    outLst = []
    def getConent(fullURL):
        content = requests.get(url=fullURL)
        formated = json.loads(content.text)
        dumpLst.append([tool, formated])
    try:
        if int(gamePort) == 0:
            for tool in toolDict.keys():
                fullURL = toolDict[tool] + infoIn
                getConent(fullURL)
        else:
            for tool in toolDict.keys():
                fullURL = toolDict[tool] + infoIn + "&port=" + gamePort
                getConent(fullURL)
    except:
        raise invalidInputInfo
    if dumpLst[0][1]["online"] == True:
        outLst.append(str("-=" * 15))
        outLst.append("Stat: Serving")
        outLst.append(f"Ping: {int(dumpLst[1][1]['duration']) / 1000000:.2f} ms")
        outLst.append(f"IP:{dumpLst[0][1]['hostname']} ({dumpLst[0][1]['ip']})")
        outLst.append(f'Port: {dumpLst[0][1]["port"]}')
        try:
            outLst.append(f'Motd Line A: {minecraftColorcodeTranslate(dumpLst[0][1]["motd"]["clean"][0]).strip()}')
        except:
            outLst.append(f'Motd Line A: NoInfo')
        try:
            outLst.append(f'Motd Line B: {minecraftColorcodeTranslate(dumpLst[0][1]["motd"]["clean"][1]).strip()}')
        except:
            outLst.append(f'Motd Line B: NoInfo')
        outLst.append(f"Players: {dumpLst[0][1]['players']['online']} / {dumpLst[0][1]['players']['max']}")
        outLst.append(str("-=" * 15))
    else:
        outLst.append(str("-=" * 15))
        outLst.append(f"IP:{dumpLst[0][1]['hostname']} ({dumpLst[0][1]['ip']})")
        outLst.append("Stat: Down")
        outLst.append(str("-=" * 15))
    return "\n".join(outLst)
# Server API End
# ---------------
# Slime Chunck Finder Start
def checkPWD(pwd):
    if pwd[-1] != "/":
        pwd = pwd + "/"
        return pwd
    else:
        return pwd
def resultSavePWD():
    saveDir = input("Image save PATH, enter 0 goes default(./):\n")
    saveFileName = input("Image filename, enter 0 goes default('slimeResult'):\n")
    if saveFileName == "0":
        saveFileName = "slimeResult"
    if saveDir == "0":
        fullDir = saveFileName + ".png"
        return fullDir
    else:
        if not os.path.exists(saveDir):
            yesNoCreatePath = input("Unknown path, create it? [y/N]")
            if yesNoCreatePath == "y":
                os.makedirs(saveDir)
                saveDir = checkPWD(saveDir)
                fullDir = saveDir + saveFileName + ".png"
                return fullDir
            else:
                print("Quitting...")
                quit()
        else:
            saveDir = checkPWD(saveDir)
            fullDir = saveDir + saveFileName + ".png"
            return fullDir
def slimeChunckFinder():
    print("Init headless Chrome...")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    baseURL = "http://mineatlas.com/?levelName=Random&seed="
    seedInput = input("Minecraft seeds:\n")
    locationX = "&mapCentreX=" + input("Location X:\n")
    locationY = "&mapCentreY=" + input("Location Y:\n")
    uselessArg = [
        "&mapZoom=18",
        "&pos=",
        "&Player=true",
        "&Spawn=true",
        "&Likely+Villages=false",
        "&Ocean+Monuments=false",
        "&Jungle+Temples=false",
        "&Desert+Temples=false",
        "&Witch+Huts=false",
        "&Slime+Chunks=true"
    ]
    otherAttri = ''.join(uselessArg)
    driver.get(baseURL + seedInput + locationX + locationY + otherAttri)
    time.sleep(15)
    webXPATH = '/html/body/div/div[2]/div[1]/div[2]'
    slimeCanvas = driver.find_element(By.XPATH,webXPATH)
    fileDir = resultSavePWD()
    slimeCanvas.screenshot(fileDir[:])
    driver.quit()
    slimeCanvasScreenShot = Image.open(fileDir[:])
    originalWidth, originalHeight = slimeCanvasScreenShot.size
    width = originalWidth / 2 - 40
    top = originalWidth / 2 - 40
    right = originalHeight / 2 + 40
    bottom = originalHeight / 2 + 40
    slimeResult = slimeCanvasScreenShot.crop((width, top, right, bottom))
    slimeResult.save(fileDir[:])
    print("Result saved to PATH:", fileDir)
# Slime Chunck Finder End
# ---------------
# Major Bug Checker Start
def majorBugGUI():
    textBlockA = tk.Label(mapiot, text = 'This may take seconds to load, pls wait', font=('Arial', 14))
    textBlockA.pack()
    homeUnpack()
    textBlockB = tk.Listbox(mapiot, yscrollcommand = scrollB.set, font=('Arial', 14), height=10, width=50)
    for eachEr in checkMajorBug():
        textBlockB.insert("end", eachEr + "\n")
    textBlockB.pack()
    # Finish loading
    textBlockA.pack_forget()
    def fucExit():
        homePack()
        buttonExit.pack_forget()
        textBlockB.pack_forget()
    buttonExit = tk.Button(mapiot, text = 'Back to home', command=fucExit)
    buttonExit.pack()
def checkMajorBug():
    mojangBugURL = "https://bugs.mojang.com/issues/"
    jqlArg = "?jql=project%20%3D%20MC%20AND%20status%20%3D%20%22In%20Progress%22%20ORDER%20BY%20votes%20DESC%2C%20updated%20DESC"
    mojangBugReportURL = mojangBugURL + jqlArg
    siteXPATH = '//*[@id="main"]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/ol'
    driver = visitSite(mojangBugReportURL)
    inProgressBugLst = driver.find_element(By.XPATH,siteXPATH)
    lstHTML = inProgressBugLst.get_attribute('innerHTML')
    bfObject = BeautifulSoup(str(lstHTML), features="lxml")
    preBugLst = bfObject.find_all('li')
    guiDisplay = []
    for preBug in preBugLst:
        guiDisplay.append(str("━" * 70))
        guiDisplay.append(f"\t[{preBug.get('data-key')}] \t{preBug.get('title')}")
    driver.quit()
    return guiDisplay
# Major Bug Checker End
# ---------------
# Spigot Resource Checker Start
def spigotCheckerGUI():
    homeUnpack()
    processLst = []
    def inCheck(usrIn):
        try:
            testA = usrIn.find("-")
        except:
            raise invalidInputInfo
        if len(usrIn) < 3:
            raise invalidInputInfo
        if usrIn == "clear":
            raise clearList
        return usrIn
    def addToProcessLst():
        try:
            processLst.append(inCheck(usrInputId.get()))
            outBlock.set("\n".join(processLst))
        except invalidInputInfo:
            outBlock.set("Invalid Resource Info")
        except clearList:
            for i in range(len(processLst)):
                processLst.pop(0)
            outBlock.set("Cleared List")
    def startThisFunc():
        try:
            outBlock.set(spigotResourceChecker(processLst))
        except invalidInputInfo:
            outBlock.set("Invalid Info")
    def seeList():
        outBlock.set("\n".join(processLst))
    # Display
    outBlock = tk.StringVar()
    outBlock.set("type in the format of <spigotID>[dash]<version>, click add")
    outLable = tk.Label(mapiot, textvariable=outBlock, font=('Arial', 14))
    outLable.pack()
    usrInputId = tk.Entry(mapiot, show=None, font=('Arial', 14))
    usrInputId.pack()
    addTrigger = tk.Button(mapiot, text = 'Add to List', command=addToProcessLst)
    addTrigger.pack()
    curLst = tk.Button(mapiot, text = 'Current List', command=seeList)
    curLst.pack()
    startIt = tk.Button(mapiot, text = 'Check', command=startThisFunc)
    startIt.pack()
    # Exit Button
    def fucExit():
        homePack()
        buttonExit.pack_forget()
        usrInputId.pack_forget()
        addTrigger.pack_forget()
        startIt.pack_forget()
        outLable.pack_forget()
        curLst.pack_forget()
    buttonExit = tk.Button(mapiot, text = 'Back to home', command=fucExit)
    buttonExit.pack()
def spigotResourceChecker(resDetail):
    returnLst = []
    try:
        for spigotPlugin in resDetail:
            versionPosition = spigotPlugin.find("-")
            versionId = spigotPlugin[versionPosition+1:]
            resId = spigotPlugin[:versionPosition]
            fullURL = "https://api.spigotmc.org/legacy/update.php?resource=" + resId
            spigotAPI = requests.get(url=fullURL)
            if str(spigotAPI.text) != versionId:
                yesOrNoUTD = "X"
            else:
                yesOrNoUTD = "√"
            returnLst.append(str("-" * 70))
            returnLst.append(f"Resource ID: {resId} | Your Version: {versionId} | Newest: {str(spigotAPI.text)} | Uptodate: {yesOrNoUTD}")
        return "\n".join(returnLst)
    except:
        return "empty list"
# Spigot Resource Checker Stop
# ---------------
# Environment Start
def chromeSetting():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "enable-automation"])
    return options
def visitSite(FullURL):
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(FullURL)
    time.sleep(2)
    return driver
def excecutePath():
    preworkPath = "C:/Program Files/mapiot" if os.name=='nt' else str(os.environ['HOME'] + "/Downloads/mapiot")
    if not os.path.exists(preworkPath):
        os.makedirs(preworkPath)
    return preworkPath + "/"
# Environment End
# ---------------
# GUI Start
def homeUnpack():
    nameDisplay.pack_forget()
    buttonMajorBugGUI.pack_forget()
    buttonQuit.pack_forget()
    buttonUUID.pack_forget()
    buttonServerAPI.pack_forget()
    buttonSpigotChecker.pack_forget()
def homePack():
    nameDisplay.pack()
    buttonMajorBugGUI.pack()
    buttonUUID.pack()
    buttonServerAPI.pack()
    buttonSpigotChecker.pack()
    buttonQuit.pack()
# GUI End
# ---------------
# Script Start
if __name__ == '__main__':
    # Headless Browser Init
    options = chromeSetting()
    # GUI Init
    mapiot = tk.Tk()
    mapiot.title("Mapiot v1.0.0")
    mapiot.geometry('500x300')
    scrollB= tk.Scrollbar(mapiot)
    scrollB.pack(side="right", fill="y")
    # Buttons
    nameDisplay = tk.Label(mapiot, text = 'Thank you for using Mapiot.', font=('Arial', 20), width=30, height=2)
    buttonUUID = tk.Button(mapiot, text = 'Player UUID Checker', command=playerUUIDgui)
    buttonMajorBugGUI = tk.Button(mapiot, text = 'Mojang Bugs Checker', command=majorBugGUI)
    buttonServerAPI = tk.Button(mapiot, text = 'Server Stats Checker', command=serverAPIgui)
    buttonSpigotChecker = tk.Button(mapiot, text = 'Spigot Resources Checker', command=spigotCheckerGUI)
    buttonQuit = tk.Button(mapiot, text = 'Quit', command=quit)
    # Button Install
    homePack()
    # GUI Loop
    mapiot.mainloop()
