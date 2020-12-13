import unittest
from masterchess import position,pieza_aliada,pawnmove,pawneat
from masterchess import rookmovehwleft,rookmovehwright,rookmovehb,rookmovehbright,rookmovevw,rookmovevb,rookmovevbdown,rookmovevwup,rookmovevwdown,rookmovehbleft,rookmovevbup
from masterchess import bishopmovewleft,bishopmovebright,bishopmovebleft,bishopmovewright,bishopmovebleftdown,bishopmovebrightdown,bishopmovewrightdown,bishopmovewleftdown,strategy
from masterchess import rookpacificmovehwleft,rookpacificmovehwright,bishoppacificmoveright,bishoppacificmoveleft

##     utility functions    ##
class masterchess_position(unittest.TestCase):
    def test_position(self):
        actual = position(60)
        esperado = (3,12)
        self.assertEqual(actual,esperado,"Should be 3,12")
    def test_position2(self):
        actual = position(110)
        esperado = (6,14)
        self.assertEqual(actual,esperado,"Should be 6,14")
    def test_position3(self):
        actual = position(0)
        esperado = (0,0)
        self.assertEqual(actual,esperado)
    def test_position4(self):
        actual = position(255)
        esperado = (15,15)
        self.assertEqual(actual,esperado)
    def test_position5(self):
        actual = position(256)
        esperado = None
        self.assertEqual(actual,esperado)
    def test_position6(self):
        actual = position(-1)
        esperado = None
        self.assertEqual(actual,esperado)
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
        self.assertEqual(actual,esperado,"False")
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
        self.assertEqual(actual,esperado,"Should be False")
    def test_pieza_aliada5(self):
        mboard="rrhhbbqq  bbhhrrrrhhbbqq  bbhh rpppppp                                        p Q   Q p    p   p         Qp   p        q   q   q                                 Q P P   P   P    Q Q   PQ   PP P  P  P P PPP PPPPP   PP  PPP  PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn="white"
        actual = pieza_aliada(mboard[255],actual_turn)
        esperado = True
        self.assertEqual(actual,esperado,"Should be True")

##           Pawn           ##
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
    def test_pawnmove4(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"black")
        esperado = ((3, 15), (5, 15))
        self.assertEqual(actual,esperado)
    def test_pawnmove5(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrr                                                                                                                                                                                                RRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawnmove6(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrr                                                                                                                                                                                                RRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawnmove7(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"black")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_pawnmove8(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawnmove(mboard,"white")
        esperado = None
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

##           Rook           ##
#Test Rook move Horizontal White
class masterchess_rookmovehwleft(unittest.TestCase):
    def test_rookmovehwleft(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehwleft(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovehwleft1(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehwleft(mboard,"white")
        esperado = ((7, 3), (7, 2))
        self.assertEqual(actual,esperado)
class masterchess_rookmovehwright(unittest.TestCase):
    def test_rookmovehwright(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehwright(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovehwright1(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehwright(mboard,"white")
        esperado = ((7, 3), (7, 4))
        self.assertEqual(actual,esperado)
#Test Rook move Vertical White         
class masterchess_rookmovevwdown(unittest.TestCase):
    def test_rookmovevwdown(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwdown(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovevwdown1(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwdown(mboard,"white")
        esperado = ((7, 3), (8, 3))
        self.assertEqual(actual,esperado)
class masterchess_rookmovevwup(unittest.TestCase):
    def test_rookmovevwup(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwup(mboard,"white")
        esperado = ((7, 3), (6, 3))
        self.assertEqual(actual,esperado)
    def test_rookmovevwup2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwup(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_rookmovevwup3(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppp                                                p                Q                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevwup(mboard,"white")
        esperado = ((8, 0), (3, 0))
        self.assertEqual(actual,esperado)
#Test Rook move Horizontal Black
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
class masterchess_rookmovehbleft(unittest.TestCase):
    def test_rookmovehbleft(self):
        mboard="              Qr                                                                                                               r                                       P                                        P                      Q        R               "
        actual = rookmovehbleft(mboard,"black")
        esperado = ((0, 15), (0, 14))
        self.assertEqual(actual,esperado)
    def test_rookmovehbleft2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehbleft(mboard,"white")
        esperado = ((1, 15), (1, 14))
        self.assertEqual(actual,esperado)
class masterchess_rookmovehbright(unittest.TestCase):
    def test_rookmovehbright(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPqPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovehbright(mboard,"black")
        esperado = ((8, 4), (8, 5))
        self.assertEqual(actual,esperado)
#Test Rook move Vertical Black
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
    def test_rookmovevbdown2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp ppppppppppppppppppppppppppppp                                                                q                                 P                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevb(mboard,"black")
        esperado = ((7, 15), (12, 15))
        self.assertEqual(actual,esperado)
    def test_rookmovevbdown3(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPqPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevbdown(mboard,"black")
        esperado = ((8, 4), (9, 4))
        self.assertEqual(actual,esperado)
class masterchess_rookmovevbup(unittest.TestCase):
    def test_rookmovevbup(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPqPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevbup(mboard,"black")
        esperado = ((8, 4), (7, 4))
        self.assertEqual(actual,esperado)
    def test_rookmovevbup2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp        ppppppppppppppp                                                                                                                 P                                PPPPPPPPPPPPPP       PRRHHBBQQqKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookmovevbup(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)

##          Bishop          ##
#Test bishop move black UP
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
#Test bishop move black Down
class masterchess_bishopmovebrightdown(unittest.TestCase):
    def test_bishopmovebrightdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp       pppppppppppppppp                                                                q             Q                                                                 PPPPPPPPPPPPPPPP       PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebrightdown(mboard,"black")
        esperado = ((7, 8), (12, 13))
        self.assertEqual(actual,esperado)
    def test_bishopmovebrightdown2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPqPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebrightdown(mboard,"black")
        esperado = ((8, 4), (9, 5))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovebleftdown(unittest.TestCase):
    def test_bishopmovebleftdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp       pppppppppppppppp                                                                q             Q                                                                 PPPPPPPPPPPPPPPP       PRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebleftdown(mboard,"black")
        esperado = ((7, 8), (13, 2))
        self.assertEqual(actual,esperado)
    def test_bishopmovebleftdown2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPqPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovebleftdown(mboard,"black")
        esperado = ((8, 4), (9, 3))
        self.assertEqual(actual,esperado)
#Test bishop move white UP
class masterchess_bishopmovewright(unittest.TestCase):
    def test_bishopmovewright1(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrp        Qppppppppppppp                                p                                                                                                                  PPPPPPPPPPPPPP       PRRHHBBQQ KBBHHRRRRHHBBQQqKBBHHRR"
        actual = bishopmovewright(mboard,"white")
        esperado = ((2, 9), (1, 10))
        self.assertEqual(actual,esperado)
    def test_bishopmovewright2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewright(mboard,"white")
        esperado = ((7, 3), (6, 4))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovewleft(unittest.TestCase):
    def test_bishopmovewleft(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewleft(mboard,"white")
        esperado = ((7, 3), (6, 2))
        self.assertEqual(actual,esperado)
#Test bishop move white Down
class masterchess_bishopmovewrightdown(unittest.TestCase):
    def test_bishopmovewrightdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppQpppppppp                                     pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewrightdown(mboard,"white")
        esperado = ((3, 1), (6, 4))
        self.assertEqual(actual,esperado)
    def test_bishopmovewrightdown2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewrightdown(mboard,"white")
        esperado = ((7, 3), (8, 4))
        self.assertEqual(actual,esperado)
class masterchess_bishopmovewleftdown(unittest.TestCase):
    def test_bishopmovewleftdown(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppppppppppppppppppppppQ                                     pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewleftdown(mboard,"white")
        esperado = ((3, 10), (2, 11))
        self.assertEqual(actual,esperado)
    def test_bishopmovewleftdown2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppQppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishopmovewleftdown(mboard,"white")
        esperado = ((7, 3), (6, 4))
        self.assertEqual(actual,esperado)

##      Pacific moves       ##
class masterchess_rookpacificmovehwleft(unittest.TestCase):
    def test_rookpacificmovehwleft(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp             Q                        pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookpacificmovehwleft(mboard,"white")
        esperado = ((4, 7), (4, 6))
        self.assertEqual(actual,esperado)
    def test_rookpacificmovehwleft2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookpacificmovehwleft(mboard,"black")
        esperado = ((5, 3), (5, 2))
        self.assertEqual(actual,esperado)
class masterchess_rookpacificmovehwright(unittest.TestCase):
    def test_rookpacificmovehwright(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp             Q                        pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookpacificmovehwright(mboard,"white")
        esperado = ((4, 7), (4, 8))
        self.assertEqual(actual,esperado)
    def test_rookpacificmovehwright2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = rookpacificmovehwright(mboard,"black")
        esperado = ((5, 3), (5, 4))
        self.assertEqual(actual,esperado)
class masterchess_bishoppacificmoveright(unittest.TestCase):
    def test_bishoppacificmoveright(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                     Q                pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveright(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)
    def test_bishoppacificmoveright2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         Q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveright(mboard,"white")
        esperado = ((5, 3), (4, 4))
        self.assertEqual(actual,esperado)
    def test_bishoppacificmoveright3(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveright(mboard,"black")
        esperado = ((13, 14), (12, 15))
        self.assertEqual(actual,esperado)
class masterchess_bishoppacificmoveleft(unittest.TestCase):
    def test_bishoppacificmoveleft(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                     Q                pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveleft(mboard,"white")
        esperado = ((4, 15), (3, 14))
        self.assertEqual(actual,esperado)
    def test_bishoppacificmoveleft2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         Q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveleft(mboard,"white")
        esperado = ((5, 3), (4, 2))
        self.assertEqual(actual,esperado)
    def test_bishoppacificmoveleft3(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppp                         q            pppppppp                            PPPPPPPPPPPPP                                                               PPPPPPPPPPPPPPqPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = bishoppacificmoveleft(mboard,"black")
        esperado = ((13, 14), (12, 13))
        self.assertEqual(actual,esperado)

#change with the strategy
class masterchess_strategy(unittest.TestCase):
    def test_strategy(self):
        mboard = "Q             RQ                                                                                                                                                                                                                               Rq HHBBQQKKBBHHRR"
        actual = strategy(mboard,"white")
        esperado = ((0, 0), (15, 0))
        self.assertEqual(actual,esperado)


if __name__ == "__main__":
    unittest.main()