import unittest
from masterchess import position,pieza_aliada,pawnmove,pawneat,rookmovehw,rookmovehb,rookmovevw,rookmovevb,rookmovevwup,rookmovevwdown,bishopmovebright,bishopmovebleft,bishopmovewright,bishopmovebleftdown,bishopmovebrightdown,bishopmovewrightdown,bishopmovewleftdown,strategy

class masterchess_position(unittest.TestCase):
    def test_position(self):
        actual = position(60)
        esperado = (3,12)
        self.assertEqual(actual,esperado,"Should be 3,12")
    def test_position2(self):
        actual = position(110)
        esperado = (6,14)
        self.assertEqual(actual,esperado,"Should be 6,14")
class masterchess_pieza_aliada(unittest.TestCase):
    def test_pieza_aliada(self):
        mboard="rrhhbbqq  bbhhrrrrhhbbqq  bbhh rpppppp                                        p Q   Q p    p   p         Qp   p        q   q   q                                 Q P P   P   P    Q Q   PQ   PP P  P  P P PPP PPPPP   PP  PPP  PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn="white"
        actual = pieza_aliada(mboard[186],actual_turn)
        esperado = True
        self.assertEqual(actual,esperado,"Should be True")
    def test_pieza_aliada2(self):
        mboard="rrhhbbqq  bbhhrrrrhhbbqq  bbhh rpppppp                                        p Q   Q p    p   p         Qp   p        q   q   q                                 Q P P   P   P    Q Q   PQ   PP P  P  P P PPP PPPPP   PP  PPP  PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn="black"
        actual = pieza_aliada(mboard[186],actual_turn)
        esperado = False
        self.assertEqual(actual,esperado,"Should be True")
    def test_pieza_aliada3(self):
        mboard="rrhhbbqq  bbhhrrrrhhbbqq  bbhh rpppppp                                        p Q   Q p    p   p         Qp   p        q   q   q                                 Q P P   P   P    Q Q   PQ   PP P  P  P P PPP PPPPP   PP  PPP  PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn="black"
        actual = pieza_aliada(mboard[0],actual_turn)
        esperado = True
        self.assertEqual(actual,esperado,"Should be True")
    def test_pieza_aliada4(self):
        mboard="rrhhbbqq  bbhhrrrrhhbbqq  bbhh rpppppp                                        p Q   Q p    p   p         Qp   p        q   q   q                                 Q P P   P   P    Q Q   PQ   PP P  P  P P PPP PPPPP   PP  PPP  PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn="black"
        actual = pieza_aliada(mboard[255],actual_turn)
        esperado = False
        self.assertEqual(actual,esperado,"Should be True")
class masterchess_pawnmove(unittest.TestCase):
    def test_pawnmove(self):
        mboard = "  Qhbbqqkkbbhhrr   hbbqq kbbhhrr                                                                  p               Q                                                            P                PPPPPPPPPPPP  P PPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn = "white"
        actual = pawnmove(mboard,actual_turn)
        esperado = ((10, 15), (9, 15))
        self.assertEqual(actual,esperado)
    def test_pawnmove2(self):
        mboard = "  Qhbbqqkkbbhhrr   hbbqq kbbhhrr                                                                  p               Q                                                            P                PPPPPPPPPPPP  P PPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn = "black"
        actual = pawnmove(mboard,actual_turn)
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawnmove3(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"white")
        esperado = ((12,0),(10,0))
        self.assertEqual(actual,esperado)
class masterchess_pawneat(unittest.TestCase):
    def test_pawneat(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpp ppp  ppppppp                                       p           p            pq qqq  qq qq qqqQ      Q      Q          q q q q  q             PPP                                PPPPPPPPPPPPP   H  QQKKBBHHRR     qQQKKBBHHRR"
        actual = pawneat(mboard,"white")
        esperado = ((11, 1), (10, 2))
        self.assertEqual(actual,esperado)
    def test_pawneat2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneat(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawneat3(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppp                                pp                p                p                Q    QQQQQQQQQQQQQQQQ P                                                                PPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneat(mboard,"black")
        esperado = ((6, 10), (7, 11))
        self.assertEqual(actual,esperado)
    def test_pawneat4(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpp ppp  ppppppp                                       p           p            pq qqq  qq qq qqqQ      Q      Q          q q q q  q             PPP                                PPPPPPPPPPPPP   H  QQKKBBHHRR     qQQKKBBHHRR"
        actual = pawneat(mboard,"white")
        esperado = ((11, 1), (10, 2))
        self.assertEqual(actual,esperado)
    def test_pawneat5(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpp ppp  ppppppp                                       p           p            pq qqq  qq qq qqqQ      Q      Q          q q q q  q             PPP                                PPPPPPPPPPPPP   H  QQKKBBHHRR     qQQKKBBHHRR"
        actual = pawneat(mboard,"white")
        esperado = ((11, 1), (10, 2))
        self.assertEqual(actual,esperado)
    def test_pawneat6(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneat(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawneat7(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneat(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
class masterchess_rookmovehw(unittest.TestCase):
    def test_rookmovehw(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehw(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)

class masterchess_rookmovehb(unittest.TestCase):
    def test_rookmovehb(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehb(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovehb2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppp                                 Q                              q                                                                 PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehb(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
class masterchess_rookmovevwdown(unittest.TestCase):
    def test_rookmovevwdown(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwdown(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
class masterchess_rookmovevwup(unittest.TestCase):
    def test_rookmovevwup(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwup(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovevwup2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppp                                                p                Q                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwup(mboard,"white")
        esperado = ((8, 0), (3, 0))
        self.assertEqual(actual,esperado)
class masterchess_rookmovevw(unittest.TestCase):
    def test_rookmovevw(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevw(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)

class masterchess_rookmovevb(unittest.TestCase):
    def test_rookmovevb(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevb(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
class masterchess_rookmovevbdown(unittest.TestCase):
    def test_rookmovevbdown(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp ppppppppppppppppppppppppppppp                                                                q                                 P                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevb(mboard,"black")
        esperado = ((7, 15), (12, 15))
        self.assertEqual(actual,esperado)



class masterchess_bishopmovebright(unittest.TestCase):
    def test_bishopmovebright(self):
        mboard = "rrhhbbqqkQbbhhrrrrhhbbqqk bbhhrrp         ppppppppppppp                                                                q                                                                                  PPPPPPPPPPPPPP       PRRHHBBQQ KBBHHRRRRHHBBQQqKBBHHRR"
        actual = bishopmovebright(mboard,"black")
        esperado = ((15, 8), (14, 9))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovebleft(unittest.TestCase):
    def test_bishopmovebleft(self):
        mboard = "rrhhbbqqkQbbhhrrrrhhbbqqk bbhhrrp         ppppppppppppp                                                                q                                                                                  PPPPPPPPPPPPPP       PRRHHBBQQ KBBHHRRRRHHBBQQqKBBHHRR"
        actual = bishopmovebleft(mboard,"black")
        esperado = ((15, 8), (14, 7))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovewright(unittest.TestCase):
    def test_bishopmovewright(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp        Qppppppppppppp                                p                                                                                                                  PPPPPPPPPPPPPP       PRRHHBBQQ KBBHHRRRRHHBBQQqKBBHHRR"
        actual = bishopmovewright(mboard,"white")
        esperado = ((2, 9), (1, 10))
        self.assertEqual(actual,esperado)

class masterchess_bishopmovebrightdown(unittest.TestCase):
    def test_bishopmovebrightdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp       pppppppppppppppp                                                                q             Q                                                                 PPPPPPPPPPPPPPPP       PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebrightdown(mboard,"black")
        esperado = ((7, 8), (12, 13))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovebleftdown(unittest.TestCase):
    def test_bishopmovebleftdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp       pppppppppppppppp                                                                q             Q                                                                 PPPPPPPPPPPPPPPP       PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebleftdown(mboard,"black")
        esperado = ((7, 8), (13, 2))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovewrightdown(unittest.TestCase):
    def test_bishopmovewrightdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppQpppppppp                                     pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewrightdown(mboard,"white")
        esperado = ((3, 1), (6, 4))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovewleftdown(unittest.TestCase):
    def test_bishopmovewleftdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppQ                                     pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewleftdown(mboard,"white")
        esperado = ((3, 10), (2, 11))
        self.assertEqual(actual,esperado)

class masterchess_strategy(unittest.TestCase):
    def test_strategy(self):
        mboard = "rrhhbbqqkk Qhhrrrrhhbbqqkq  hhrrp          pppppppppppp                                                                                                                                                    PPPPPPPPPPPP        PRRHHBBQ q BBHHRRRRHHBBQ   BBHHRR"
        actual = strategy(mboard,"black")
        esperado = ((3, 6), (5, 6))
        self.assertEqual(actual,esperado)


if __name__ == "__main__":
    unittest.main()