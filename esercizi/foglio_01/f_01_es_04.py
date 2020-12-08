class Automobile:

    def __init__(self, casa_auto, modello, n_posti, n_portiere, kw, targa, categoria):
        self.casa_auto = casa_auto
        self.modello = modello
        self.n_posti = n_posti
        self.n_portiere = n_portiere
        self.kw = kw
        self.targa = targa
        self.categoria = categoria
    
    def __str__(self):
        stampa = "--- dati automobile ---\n"
        stampa += "casa_auto: " + str(self.casa_auto) + "\n"
        stampa += "modello: " + str(self.modello) + "\n"
        stampa += "n_posti: " + str(self.n_posti) + "\n"
        stampa += "n_portiere: " + str(self.n_portiere) + "\n"
        stampa += "kw: " + str(self.kw) + "\n"
        stampa += "categoria: " + str(self.categoria) + "\n"
        stampa += "targa: " + str(self.targa) + "\n"
        stampa += "----------------------"

        return stampa
    
    def parla(self):
        print("Broom Broom")
    
    def confronta(self, altra_auto):
        return (self.casa_auto == altra_auto.casa_auto) and (self.modello == altra_auto.modello) and (self.n_posti == altra_auto.n_posti) and (self.n_portiere == altra_auto.n_portiere) and (self.categoria == altra_auto.categoria)
    
    def bollo(self):

        bollo = 0

        if(self.categoria == "Euro0"):
            if(self.kw < 100):
                bollo = self.kw * 3
            else:
                bollo = self.kw * 4.50

        if(self.categoria == "Euro1"):
            if(self.kw < 100):
                bollo = self.kw * 2.50
            else:
                bollo = self.kw * 4.35
        
        if(self.categoria == "Euro2"):
            bollo = self.kw * 3
        
        return bollo



auto_0 = Automobile("casa mia", "ultimo", 5, 5, 50, "IJN2NIE21", "Euro0")
auto_1 = Automobile("casa tua", "primo", 2, 3, 500, "IJFBSI2DN", "Euro1")

print(auto_0)
auto_1.parla()
print("confronto:", auto_0.confronta(auto_1))
print("bollo:", auto_1.bollo(), "€")
