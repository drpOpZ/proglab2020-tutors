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

class Transformer(Automobile):

    def __init__(self, casa_auto, modello, n_posti, n_portiere, kw, targa, categoria, nome, generazione, grado, fazione, reparto):
        super().__init__(casa_auto, modello, n_posti, n_portiere, kw, targa, categoria)
        self.nome = nome
        self.generazione = generazione
        self.grado = grado
        self.fazione = fazione
        self.reparto = reparto
    
    def parla(self):
        if(self.fazione == "Autobots"):
            print("Noi siamo Autobots, proteggeremo ogni essere vivente")
        else:
            print("Noi siamo Decepticons e l’AllSpark sarà nostro!")
    
    def scheda_militare(self):
        stampa = "--- dati Transformer ---\n"
        stampa += "nome: " + str(self.nome) + "\n"
        stampa += "generazione: " + str(self.generazione) + "\n"
        stampa += "fazione: " + str(self.fazione) + "\n"
        stampa += "grado: " + str(self.grado) + "\n"
        stampa += "reparto: " + str(self.reparto) + "\n"
        stampa += "-----------------------"

        print(stampa)



auto_0 = Automobile("casa mia", "ultimo", 5, 5, 50, "IJN2NIE21", "Euro0")

t_0 = Transformer("Cybertron", "Camaro", 4, 5, "200", "SDFNISND", "Euro0", "Bumblebee", 5, "soldato scelto", "Autobots", "assalto")

t_1 = Transformer("Cybertron", "Mustang", 4, 5, "200", "IJDNSNJ", "Euro2", "Barricade", 5, "cacciatore", "Decepticons", "scout")

t_0.parla()
t_0.scheda_militare()

t_1.parla()
t_1.scheda_militare()

## OPZIONALE ##

print("Q1:", type(auto_0) == Automobile)
print("Q2:", issubclass(Transformer, Automobile))
print("Q3:", type(t_0) == Transformer)
print("Q4:", type(t_0) == type(t_1))
print("Q5:", isinstance(t_1, Automobile))
print("Q6:", isinstance(auto_0, Transformer))

#print("+Q6:", isinstance((Transformer)auto_0, Transformer))
