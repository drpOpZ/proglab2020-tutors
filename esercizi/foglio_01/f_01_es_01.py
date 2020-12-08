def stampa(lista):
    print("lista:", lista)

def statistiche(lista):

    risultati = [0, lista[0], lista[0], 0]
    # [somma, minimo, massimo, media]

    for item in lista:
        risultati[0] += item
        if(risultati[1] > item):
            risultati[1] = item
        if(risultati[2] < item):
            risultati[2] = item
    
    risultati[3] = risultati[0] / len(lista)
    return risultati

def controlli(l1, l2):
    if(len(l1) != len(l2)):
        return False
    
    i = 0
    while(i < len(l1)):
        if(type(l1[i]) != int):
            return False
        else:
            i += 1

    i = 0
    while(i < len(l2)):
        if(type(l2[i]) != int):
            return False
        else:
            i += 1
    
    return True

def somma_vettoriale(l1, l2):    

    if(controlli(l1, l2) == False):
        return []

    somma = []

    i = 0
    while(i < len(l1)):
        somma.append(l1[i] + l2[i])
        i += 1
    
    return somma

def prodotto_vettoriale(l1, l2):

    if(controlli(l1, l2) == False):
        return []
    
    prodotto = []

    i = 0
    while(i < len(l1)):
        prodotto.append(l1[i] * l2[i])
        i += 1
    
    return prodotto



l0 = [1, 2, 3, 4, 5]
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3]
l4 = [1, 2, "ciao", 3.39, 7]

stampa(l0)
print("statistiche:", statistiche(l1))

print("somma:", somma_vettoriale(l0, l1))
print("prodotto:", prodotto_vettoriale(l0, l1))

print("somma:", somma_vettoriale(l0, l2))
print("prodotto:", prodotto_vettoriale(l1, l4))
