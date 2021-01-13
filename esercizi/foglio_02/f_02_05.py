import numpy as np

# Dati della tabella
data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

#------------------------
# definizione del modello
#------------------------
class LinearModel():
  def __init__(self):
    # Inizializzo i campi a None
    self.train_data = None
    self.slope = None
    self.intercept = None

  def fit(self,train_data):
    # controllo che train_data sia della forma giusta
    try:
      assert(len(train_data.shape)==2)
      assert(train_data.shape[1]==2)
    except:
      raise Exception("Bad train_data shape! {} should be (*,2)".format(train_data.shape))

	  # ricavo le x e le y da train_data
    x = train_data[:,0]
    y = train_data[:,1]
    
    # Calcolo il coefficiente di correlazione (uso numpy per semplificare i calcoli)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    ustd_x = np.std(x,ddof=1)
    ustd_y = np.std(y,ddof=1)
    pearson_corr = np.sum((x-mean_x)*(y-mean_y))/np.sqrt(np.sum((x-mean_x)**2) * np.sum((y-mean_y)**2))

    # Calcolo i parametri del modello e li salvo nei campi definiti in __init__
    self.slope = pearson_corr * ustd_y / ustd_x
    self.intercept = mean_y - self.slope * mean_x
    
    # Salvo anche i train_data che ho usato per fare il fit
    self.train_data = train_data
	
    #... no return

  def predict(self,xs):
    # Lancia un eccezione se il coefficiente angolare o l'intercetta non sono none
    if self.slope is None or self.intercept is None:
      raise Exception("You need to fit your model first!")
    
    # Calcolo i valori predetti per le xs
    # Nota che anche qui sto usando numpy: xs è un ndarray (cioé un vettore di valori)
    # e le operazioni + e * vengono applicate a tutti i valori al suo interno.
    # Nel testo dell'esercizio trovate la spiegazione di come funziona la cosa.
    predictions = self.intercept + xs*self.slope
    
    return predictions

#-------------------------
# applicazione del modello
#-------------------------

# Istanzio il modello
modello = LinearModel()

# Effetuo il fit ("data" è definito all'inizio dello script)
modello.fit(data)

# Predico il numero di litri per il tragitto stimato
km_tragitto = 2500
litri_tragitto = modello.predict(km_tragitto)

# calcolo la spesa di ciascuno
prezzo_benzina = 1.4
quota_individuale = litri_tragitto*prezzo_benzina/3

# Stampa i risultati a schermo
print("Litri di benzina totali:\t{:.2f} lt\nQuota individuale:\t\t{:.2f} €".format(litri_tragitto,quota_individuale))

#-------------
# EXTRA: Plot
#-------------
print("\n-EXTRA-")

# Libreria per fare i plot
import matplotlib.pyplot as plt

# mi stampo i parametri del modello a schermo
print("Parametri del modello:\nm =\t{}\nq =\t{}".format(modello.slope,modello.intercept))

# Imposto la figura
fig,ax = plt.subplots()
fig.set_dpi(150)
plt.grid()

# plotto i dati originali in blu
ax.scatter(data[:,0],data[:,1], color="b")
# plotto il valore predetto in rosso
ax.scatter(km_tragitto,litri_tragitto, color="r")

# plotto la retta del modello. Uso due valori scelti da me a occhio per far si
# che la retta sia abbastanza lunga
valori = np.array([0,3000])
ax.plot(valori, modello.predict(valori),color="green")

# imposto le etichette degli ass
ax.set_xlabel("km percorsi")
ax.set_ylabel("lt benzina")

# mostro il grafico
plt.show()
