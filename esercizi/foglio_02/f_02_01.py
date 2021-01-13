import random

class Automa:

    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None

    def exe_biancheria(self):
        risultato = random.choices([False, True], weights = (10, 90), k = 1)
        return risultato[0]

    def set_biancheria(self):
        self.biancheria = True

    def exe_calzini(self):
        risultato = random.choices([False, True], weights = (10, 90), k = 1)
        return risultato[0]

    def set_calzini(self):
        self.calzini = True

    def exe_maglia(self):
        risultato = random.choices([False, True], weights = (10, 90), k = 1)
        return risultato[0]

    def set_maglia(self):
        self.maglia = True

    def exe_pantaloni(self):
        risultato = random.choices([False, True], weights = (10, 90), k = 1)
        return risultato[0]

    def set_pantaloni(self):
        self.pantaloni = True

    def exe_calzatura(self):
        risultato = random.choices([False, True], weights = (10, 90), k = 1)
        return risultato[0]

    def set_calzatura(self):
        self.calzatura = True     


def esegui(automa, capo):

    risultato = None

    if(capo == "biancheria"):
        risultato = automa.exe_biancheria()
    
    if(capo ==  "calzini"):
        risultato = automa.exe_calzatura()

    if(capo == "maglia"):
        risultato = automa.exe_maglia()

    if(capo == "pantaloni"):
        risultato = automa.exe_pantaloni()

    if(capo == "calzatura"):
        risultato = automa.exe_calzatura()

    return risultato

def imposta(automa, capo):

    if(capo == "biancheria"):
        automa.set_biancheria()
    
    if(capo ==  "calzini"):
        automa.set_calzatura()

    if(capo == "maglia"):
        automa.set_maglia()

    if(capo == "pantaloni"):
        automa.set_pantaloni()

    if(capo == "calzatura"):
        automa.set_calzatura()


automa = Automa()

vestiario_fix = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]
vestiario_var = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]

vestito = True
i = 0

while(vestito):

    capo = vestiario_fix[i]
    print("capo:", capo)

    if(capo == random.choice(vestiario_var)):
        vestiario_var.pop(0)
        print("[SUCCESSO] automa segue la procedura")
    else:
        print("[FALLIMENTO] automa non sta seguendo la procedura")
        continue
    
    risultato_exe = esegui(automa, capo)

    if(risultato_exe == True):
        print("[SUCCESSO] automa ha indossato il capo:", capo)
        imposta(automa, capo)
    else:
        raise Exception("[FALLIMENTO CRITICO] automa non è riuscito ad indossare il capo:", capo)

    if not vestiario_var:
        vestito = False
    else:
        i += 1

print("[SUCCESSO TOTALE] automa si è vestito correttamente")
