import lib
import errorClasses as er

class spigotAPI(object):
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