DESNO, GOR, DOL, LEVO = 'desno', 'gor', 'dol', 'levo'

class Kaca:
    def __init__(self, tocke, smer=DESNO):
        self.tocke = tocke
        self.smer = smer

    def __repr__(self):
        return 'Kaca({}, smer={})'.format(self.tocke, self.smer.upper())

    def premakni(self):
        del self.tocke[-1]
        glava_x, glava_y = self.tocke[0]
        if self.smer == DESNO:
            glava_x += 1
        elif self.smer == GOR:
            glava_y += 1
        elif self.smer == DOL:
            glava_y -= 1
        elif self.smer == LEVO:
            glava_x -= 1
        self.tocke.insert(0, (glava_x, glava_y))

    def zamenjaj_smer(self, nova_smer):
        self.smer = nova_smer


