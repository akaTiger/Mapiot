from asyncio import exceptions
import lib
import errorClasses as er
import urllib.parse

class linkGen(object):
    def __init__(self):
        self._head = lib.getSpigotUrlHead()
        self._nameLib = [i[0] for i in lib.getParameters().values()]
        self._funcLib = lib.getParameters()
    
    def numIdCheck(self, checkItem: str):
        try:
            assert checkItem != ""
        except:
            raise er.parameterMissing
        try:
            assert checkItem.isnumeric() is True
            if int(checkItem) > 0:
                pass
        except:
            raise er.parameterError
        
    
    def listResources(self, get: str):
        try:
            # assertation
            for i in get:
                assert i.isalpha() is False
        except:
            raise er.parameterError
        if len(get) > 0:
            l = get.split(",")
            if len(l) == 1:
                suf = "&category=" + str(l[0])
                arg = self._head + "?action=" + self._funcLib[0][1] + suf
                return arg
            elif len(l) == 2:
                suf = "&category=" + str(l[0]) + "&page=" + str(l[1])
                arg = self._head + "?action=" + self._funcLib[0][1] + suf
                return arg
            else:
                raise er.parameterError
        else:
            arg = self._head + "?action=" + self._funcLib[0][1]
            return arg
    
    def getResource(self, get: str):
        # Example: https://api.spigotmc.org/simple/0.2/index.php?action=getResource&id=2
        if True:
        # Get Check
            self.numIdCheck(checkItem=get)
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[1][1]),
                ("id", get)
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def getResourcesByAuthor(self, get: tuple):
        # Example: https://api.spigotmc.org/simple/0.2/index.php?action=getResourcesByAuthor&id=100356&page=1
        if True:
        # Get Check
            if len(get) == 1:
                pageTo = 1
            elif len(get) == 2:
                pageTo = get[1]
            else:
                raise er.parameterError
            self.numIdCheck(get[0])
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[2][1]),
                ("id", get[0]),
                ("page", pageTo)
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def listResourceCategories(self):
        # Example: https://api.spigotmc.org/simple/0.2/index.php?action=listResourceCategories
        if True:
        # Get Check
            pass
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[3][1])
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def getResourceUpdate(self, get: str):
        # Example: https://api.spigotmc.org/simple/0.2/index.php?action=getResourceUpdate&id=352711
        if True:
        # Get Check
            self.numIdCheck(checkItem=get)
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[4][1])
                ("id", get)
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def getResourceUpdates(self, get: str):
        # Example: 
        if True:
        # Get Check
            pass
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[][])
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def getAuthor(self, get: str):
        # Example: 
        if True:
        # Get Check
            pass
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[][])
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)
    def findAuthor(self, get: str):
        # Example: 
        if True:
        # Get Check
            pass
        if True:
        # Build URL
            queryParameters = [
                ("action", self._funcLib[][])
            ]
        return self._head + "?" + urllib.parse.urlencode(queryParameters)