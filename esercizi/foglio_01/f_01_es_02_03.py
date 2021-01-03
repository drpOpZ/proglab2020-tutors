# importo il modulo per gestire le date
from datetime import datetime

class CSVFile():

    def __init__(self,name):
        self.name = name

    # Metodo che stampa l'header del file
    def __str__(self):
        my_file = open(self.name, "r")

        # Leggo la prima linea 
        return my_file.readline()

    def get_date_vendite(self):

        # Inizializzo una lista vuota per salvare le date
        dates = []

        # Apro e leggo il file, linea per linea
        my_file = open(self.name, "r") 
        for line in my_file:
   
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')

            # Se NON sto processando l’intestazione...
            if elements[0] != 'Date':

                # Setto il valore della data
                my_date = datetime.strptime(elements[0], '%d-%m-%Y')

                # Aggiungo alla lista dei valori questo valore
                dates.append(my_date)
        return dates

file = CSVFile("shampoo_sales.csv")

# stampo l'header del file
print("The header of the file is:", file)

date_vendite = file.get_date_vendite()

# stampo le date delle venidte
for data in date_vendite:
    print(data.strftime('%d-%m-%Y'))