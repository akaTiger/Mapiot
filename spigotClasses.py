import lib
import errorClasses as er

class linkGen(object):
    def __init__(self):
        self._head = "https://api.spigotmc.org/simple/0.2/index.php"
        self._nameLib = [i[0] for i in lib.getParameters().values()]
        self._funcLib = lib.getParameters()
    
    def listResources(self, get: str):
        if True:
            # assertation
            for i in get:
                assert i.isalpha() is False
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
        pass
    def getResourcesByAuthor(self, get: str):
        pass
    def listResourceCategories(self, get: str):
        pass
    def getResourceUpdate(self, get: str):
        pass
    def getResourceUpdates(self, get: str):
        pass
    def getAuthor(self, get: str):
        pass
    def findAuthor(self, get: str):
        pass