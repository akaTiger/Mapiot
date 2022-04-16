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
            return self.javaRandomNextInt(10) == 0, str(mcAlgorA), str(mcAlgorB), str(mcAlgorC), str(mcAlgorD), str(self.seed)

