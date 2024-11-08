# Inizializziamo una variabile per la somma
somma = 0

# Ciclo che continua finché l'utente non inserisce 0
while True:
    # Chiediamo all'utente di inserire un numero
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    # Se l'utente inserisce 0, usciamo dal ciclo
    if numero == 0:
        break
    
    # Aggiungiamo il numero alla somma
    somma += numero

# Alla fine, stampiamo la somma dei numeri
print(f"La somma di tutti i numeri inseriti è: {somma}")
