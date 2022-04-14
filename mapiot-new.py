class pythonMinecraftSlimeChecker(object):
    def __init__(self, cmd):
        if cmd == "start":
            
            
        
        
        
        
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
    def nextInt(self, n = None):
        if n is None:
            return self.next(32)
        if n <= 0:
            raise ValueError("Argument must be positive!")
        if not (n & (n - 1)):
            return (n * self.next(31)) >> 31
        bits = self.next(31)
        val = bits % n
        while (bits - val + n - 1) < 0:
            bits = self.next(31)
            val = bits % n
        return val
    def doCheck(self, gameSeed, xPosition, zPosition):
        javaIntLimit = 2147483647
        javaLongLimit = 9223372036854775807
        mcAlgorA = self.int_overflow(self.int_overflow(xPosition * xPosition * 0x4c1906, javaIntLimit), javaLongLimit)
        mcAlgorB = self.int_overflow(self.int_overflow(xPosition * 0x5ac0db, javaIntLimit), javaLongLimit)
        mcAlgorC = self.int_overflow((self.int_overflow(zPosition * zPosition, javaIntLimit) * 0x4307a7), javaLongLimit)
        mcAlgorD = self.int_overflow((self.int_overflow(zPosition * 0x5f24f, javaIntLimit)), javaLongLimit)
        processA = (self.int_overflow(((gameSeed + mcAlgorA + mcAlgorB + mcAlgorC + mcAlgorD )^ 0x3ad8025f), javaLongLimit))
        self.seed = processA
        return str(self.nextInt(10) == 0)

if __name__ == "__main__":
    pythonMinecraftSlimeChecker("start")