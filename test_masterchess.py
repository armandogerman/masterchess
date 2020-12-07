import unittest
from turn import position,pieza_aliada,pawneat,pawneatw,pawneatb,pawnmove,calc,select_pawn

class turn_position(unittest.TestCase):
    def test_position(self):
        actual = position(60)
        esperado = (3,12)
        self.assertEqual(actual,esperado,"Should be 3,12")
    def test_position2(self):
        actual = position(110)
        esperado = (6,14)
        self.assertEqual(actual,esperado,"Should be 6,14")

class turn_pieza_aliada(unittest.TestCase):
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

class turn_pawneat(unittest.TestCase):
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

class turn_pawneatw(unittest.TestCase):
    def test_pawneatw(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpp ppp  ppppppp                                       p           p            pq qqq  qq qq qqqQ      Q      Q          q q q q  q             PPP                                PPPPPPPPPPPPP   H  QQKKBBHHRR     qQQKKBBHHRR"
        actual = pawneatw(mboard,"white")
        esperado = ((11, 1), (10, 2))
        self.assertEqual(actual,esperado)
    def test_pawneatw2(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpp ppp  ppppppp                                       p           p            pq qqq  qq qq qqqQ      Q      Q          q q q q  q             PPP                                PPPPPPPPPPPPP   H  QQKKBBHHRR     qQQKKBBHHRR"
        actual = pawneatw(mboard,"white")
        esperado = ((11, 1), (10, 2))
        self.assertEqual(actual,esperado)
    def test_pawneatw3(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneatw(mboard,"white")
        esperado = None
        self.assertEqual(actual,esperado)

class turn_pawneatb(unittest.TestCase):
    def test_pawneatb(self):
        mboard = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrppppppp                                pp                p                p                Q    QQQQQQQQQQQQQQQQ P                                                                PPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = pawneatb(mboard,"black")
        esperado = ((6, 10), (7, 11))
        self.assertEqual(actual,esperado)

class turn_pawnmove(unittest.TestCase):
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

class turn_select_pawn(unittest.TestCase):
    def select_pawn(self):
        mboard = "  Qhbbqqkkbbhhrr   hbbqq kbbhhrr                                                                  p               Q                                                            P                PPPPPPPPPPPP  P PPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn = "white"
        actual = select_pawn(mboard,actual_turn)
        esperado = ((10, 15), (9, 15))
        self.assertEqual(actual,esperado)

class turn_calc(unittest.TestCase):
    def test_calc(self):
        mboard = "  Qhbbqqkkbbhhrr   hbbqq kbbhhrr                                                                  p               Q                                                            P                PPPPPPPPPPPP  P PPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual_turn = "white"
        actual = calc(mboard,actual_turn)
        esperado = ((10, 15), (9, 15))
        self.assertEqual(actual,esperado)
    def test_calc2(self):
        mboard="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        actual = calc(mboard,"white")
        esperado = ((12,0),(10,0))
        self.assertEqual(actual,esperado)

if __name__ == "__main__":
    unittest.main()