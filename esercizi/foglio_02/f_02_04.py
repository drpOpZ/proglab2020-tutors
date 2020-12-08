import math

# funzione esterna (usata per sanitizzare)
def conversione(a):

    conversione = False
    if(type(a) == str):
        
        try:
            a = int(a)
            conversione = True
        except:
            print("a =", a, "non è un intero")

        if(conversione != True):
            try:
                a = float(a)
            except:
                raise Exception("a = " + a + ", non è un convertibile")

    return a


# classe Calcolatrice
class Calcolatrice:

    def somma(a, b):

        a = conversione(a)
        b = conversione(b)

        if(type(a) == type(b)):
            return a + b
        else:
            return None
    
    def sottrazione(a, b):

        a = conversione(a)
        b = conversione(b)

        if(type(a) == type(b) and type(a) != str):
            return a - b
        else:
            return None

    def prodotto(self, a, b):

        a = conversione(a)
        b = conversione(b)

        if(type(a) == type(b)):
            return a * b
        else:
            return None  

    def divisione(self, a, b):

        a = conversione(a)
        b = conversione(b)

        if(type(a) == type(b) and b != 0):
            return a / b
        else:
            return None 

    def modulo(self, a):

        a = conversione(a)

        if a < 0:
            return -a
        else:
            return a                

    def potenza(self, a, b):

        a = conversione(a)
        b = conversione(b)

        b = Calcolatrice.modulo(self, b)

        if(type(b) == int):
            return a ** b
        else:
            print("[ERRORE] la potenza non può essere decimale:", b)
            return None        

    def radice(self, a):
          
        radx = None  
        a = conversione(a)
        a = Calcolatrice.modulo(self, a)
        
        try:
            radx = math.pow(a, 0.5)
        except:
            print("[ERRORE] operazione di radice non riuscita")

        return radx

    def conversione_base(self, val, base):
        
        val = conversione(val)
        base = conversione(base)

        divisione = True
        resti = []

        while(divisione):
            val = int(val)
            if(val != 1):
                resti.append(val % base)
                val = val / base
            else:
                resti.append(val % base)
                divisione = False

        # per invertire l'ordine degli item in una lista
        resti_rev = []
        for value in resti[::-1]:
            resti_rev.append(value)

        # per convertire una lista in una stinga
        strings = [str(integer) for integer in resti_rev]
        convertito = "".join(strings)  

        return convertito
              

# classe Test
class Test:

    def test_somma(self):
        if(Calcolatrice.somma(1, 1) != 2):
            raise Exception("[ERRORE] somma(1, 1) non uguale a 2")

        if(Calcolatrice.somma(1, "2") != 3):
            raise Exception("[ERRORE] somma(1, '2') non uguale a 3")

        if(Calcolatrice.somma("3", "2") != 5):
            raise Exception("[ERRORE] somma('3', '2') non uguale a 5")

        if(Calcolatrice.somma(1, "mela") != 3):
            raise Exception("[ERRORE] somma(1, 'mela') non uguale a (?)")

    def test_sottrazione(self):
        if(Calcolatrice.sottrazione(1, 2) != -1):
            raise Exception("[ERRORE] sottrazione(1, 2) non uguale a -1")

    def test_prodotto(self):
        if(Calcolatrice.prodotto(1, "2") != 2):
            raise Exception("[ERRORE] prodotto(1, '2') non uguale a 2")

    def test_divisione(self):
        if(Calcolatrice.divisione(1, "2") != 0.5):
            raise Exception("[ERRORE] prodotto(1, '2') non uguale a 0.5")

    def test_modulo(self):
        if(Calcolatrice.modulo(-5), 5):
            raise Exception("[ERRORE] modulo(-5) non uguale a 5")

    def test_potenza(self):
        if(Calcolatrice.potenza(2.1, 2) != 4.41):
            raise Exception("[ERRORE] potenza(2.1, 2) non uguale a 4.41")

        if(Calcolatrice.potenza(-2.1, 3), -9.26):
            raise Exception("[ERRORE] potenza(-2.1, 3) non uguale a -9.26")

    def test_radice(self):
        if(Calcolatrice.radice(2), 1.41):
            raise Exception("[ERRORE] radice(2) non uguale a 1.41")

        if(Calcolatrice.radice(-3), 1.73):
            raise Exception("[ERRORE] somma(-3) non uguale a 1.73")

    def test_conversione(self):
        if(Calcolatrice.conversione_base(10, 2), "1010"):
            raise Exception("[ERRORE] conversione(10, 2) non uguale a 1010")


# parte principale dello script
test_calc = Test()

print("inizio dei test...")
test_calc.test_somma()
test_calc.test_sottrazione()
test_calc.test_prodotto()
test_calc.test_divisione()
test_calc.test_modulo()
test_calc.test_potenza()
test_calc.radice()
test_calc.test_conversione()
print("fine dei test!")
