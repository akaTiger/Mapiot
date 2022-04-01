import requests
import json

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
        
def formatUUID(uuid):
    outLst = [alphabit for alphabit in uuid if alphabit != "-"]
    return "".join(outLst)

def testUUID(uuid):
    fullURL = "https://api.minetools.eu/profile/" + uuid
    content = requests.get(url=fullURL)
    result = json.loads(content.text)
    if str(result["decoded"]) == "None":
        return False
    else:
        return True

if __name__ == '__main__':
    print("MinecraftAPI 集合工具")
    print("查询值可为服务器地址、玩家uuid")
    infoIn = input("输入查询值:\n")
    infoType = "MCID"
    if len(infoIn) >= 9:
        if infoIn[8] == "-":
            infoType = "UUID"
        for alphabit in infoIn:
            if alphabit == ".":
                infoType = "serverIP"
                break
    else:
        for alphabit in infoIn:
            if alphabit == ".":
                infoType = "serverIP"
                break
    if infoType == "serverIP":
        gamePort = int(input("输入服务器端口 (默认请输入0) :\n"))
        toolDict = {
            "mcsrvstat": "https://api.mcsrvstat.us/2/",
            "mcapi": "https://mcapi.us/server/status?ip=",
        }
        dumpLst = []
        if gamePort == 0:
            for tool in toolDict.keys():
                fullURL = toolDict[tool] + infoIn
                content = requests.get(url=fullURL)
                formated = json.loads(content.text)
                dumpLst.append([tool, formated])

        if dumpLst[0][1]["online"] == True:
            print("-=" * 15)
            print("状态:", "正常服务中")
            print("延迟:" , f"{int(dumpLst[1][1]['duration']) / 1000000:.2f} 毫秒")
            print("IP地址:", f"{dumpLst[0][1]['hostname']} ({dumpLst[0][1]['ip']})")
            print("游戏端口:", dumpLst[0][1]["port"])
            print("游戏标语第一行:", minecraftColorcodeTranslate(dumpLst[0][1]["motd"]["clean"][0]).strip())
            print("游戏标语第二行:", minecraftColorcodeTranslate(dumpLst[0][1]["motd"]["clean"][1]).strip())
            print("玩家:", f"{dumpLst[0][1]['players']['online']} / {dumpLst[0][1]['players']['max']}")
            print("-=" * 15)
        else:
            print("-=" * 15)
            print("IP地址:", f"{dumpLst[0][1]['hostname']} ({dumpLst[0][1]['ip']})")
            print("状态:", "离线")
            print("-=" * 15)
    elif infoType == "UUID":
        toolDict = {
            "MoJangAPI": "https://api.mojang.com/user/profiles/",
            "MineToolsEU": "https://api.minetools.eu/profile/"
        }
        while True:
            if testUUID(infoIn) is False:
                infoIn = input("UUID 输入有误, 重新输入或输入q退出:")
                if infoIn == "q":
                    quit()
            else:
                break
        dumpLst = []
        for tool in toolDict.keys():
            if tool == "MoJangAPI":
                infoNeeded = formatUUID(infoIn)
                FullURL = toolDict[tool] + infoNeeded + "/names"
                content = requests.get(url=FullURL)
                nameLst = json.loads(content.text)
                if len(nameLst) > 1:
                    infoA = "游戏ID: " + nameLst[-1]["name"]
                    previousName = []
                    for name in nameLst[:-1]:
                        previousName.append(name["name"])
                    infoB = "曾经使用过的游戏ID: " + "; ".join(previousName)
                if len(nameLst) == 1:
                    infoA = "游戏ID: " + nameLst[0]["name"]
            else:
                fullURL = toolDict[tool] + infoIn
                content = requests.get(url=fullURL)
                formated = json.loads(content.text)
                dumpLst.append([tool, formated])
        print("-=" * 15)
        print(infoA)
        print(infoB)
        print("披风URL:", dumpLst[0][1]["decoded"]["textures"]["CAPE"]["url"])
        print("皮肤URL:", dumpLst[0][1]["decoded"]["textures"]["SKIN"]["url"])
        print("-=" * 15)
