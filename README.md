# mapiot
Minecraft API Organization Tool

##### Supported Functions

- Convert UUID to player infos
- Get server status through server's ip address
- Slime chunk checker
- Mojang bug notifier
- Spigot resource update checker

##### Environment

- python3
- pip3
- pip-requests
- pip-pillow
- pip-selenium
- pip-webdriver_manager
- pip-beautifulsoup

##### Usage

```
python3 mapiot.py

Mapiot stands for Minecraft API organization tool
[0] UUID
[1] serverIP
[2] slimeChecker
[3] bugChecker
[4] spigotResourceChecker
Choose what to do:

user@computer% 1
```

###### UUID

```
Type in player UUID, accept any form:
user@computer% 62edca7f-0797-4414-81d1-8269fae23b11
```

```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Current ID: LilT1ger
Used IDs: YICHENG_DING; Tai_ger
Cape URL: http://textures.minecraft.net/texture/2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933
Skin URL: http://textures.minecraft.net/texture/a72b840c5bbb3c1dff8a7cb84d0de64ff3f1cafa5b4b25b5ded10b57cccda2ec
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

###### serverIP

```
Server IP address:
user@computer% play.hypixel.net
Server port, enter 0 indicate default(25565):
user@computer% 0

Lookup in Progress...
```

```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Stat: Serving
Ping: 46.48 ms
IP: play.hypixel.net (172.65.210.190)
Port: 25565
Motd Line A: Hypixel Network [1.8-1.18]
Motd Line B: NEW PROTOTYPE GAME: WOOL WARS!
Players: 52374 / 200000
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

###### slimeChecker

```
Minecraft seeds:
user@computer% 933819295039
Location X:
user@computer% 2211
Location Y:
user@computer% 3920

Visiting Mineatlas... Wait for 15 seconds...

Image save PATH, enter 0 goes default(./):
user@computer% /Users/tiger/Downloads/pythonMinecraft
Image filename, enter 0 goes default('slimeResult'):
user@computer% 0
Unknown path, create it? [y/N]
user@computer% y

Image processing...
Result saved to PATH: /Users/tiger/Downloads/pythonMinecraft/slimeResult.png
```

![slimeResult](https://tigerdingcom-1258728659.cos.ap-shanghai.myqcloud.com/Github/slimeResult.png)

Image saved is a chunk indicator that has a size of 5 by 5. The location that the script asked before is located in the center of this image. Green boxs are avtive slime chunks.

> This function is only worked in Minecraft JE. Glitches may happend in the newest version.

###### bugChecker

```
Visiting Mojang... Wait for 5 seconds...

-----------
[MC-249712] Server hangs and game stops responding when loading a chunk containing a structure with an allay
-----------
[MC-177878] Zoglins uselessly attack the wither
-----------
[MC-162633] Zombified piglins don't do damage to Wither
-----------
[MC-184330] Skeleton arrows fail to hit the wither

.....
```

This function will display all the **in progress** bug that listed in  `bug.mojang.com/issues/` . This script will print out the issue ids and bug title, sorted in amount of user votes.

###### spigotResourceUpdateChecker

```
Type in the full PATH of spigot resource id list (file path has to be end with a .txt file):
user@computer% /Users/tiger/Downloads/lol.txt

----------------------------------------------------------------------
Resource ID: 8117 | Your Version: 4.2.0 | Newest: 4.2.0 | Uptodate: √
----------------------------------------------------------------------
Resource ID: 98630 | Your Version: 1.4 | Newest: 1.4 | Uptodate: √
----------------------------------------------------------------------
Resource ID: 96398 | Your Version: 1.1 | Newest: 1.1 | Uptodate: √
----------------------------------------------------------------------
Resource ID: 70386 | Your Version: 1.5.1 | Newest: 1.5.2 | Uptodate: X
----------------------------------------------------------------------
Resource ID: 48655 | Your Version: 3.6.3 | Newest: 3.6.3 | Uptodate: √
```

```
<!-- lol.txt -->
8117-4.2.0
98630-1.4
96398-1.1
70386-1.5.1
48655-3.6.3
resource_id[dash]your_version

```

Spigot resource id can get from the URL, usually appears after the project name. Don't forget to add a blank line at the end of the txt file or the script will break.



*All informations you can get from this script is public accessable, APIs are supported by external sites and you get it by request it using your own ip. More feature will come out in the future.* 
