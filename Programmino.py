# Messaggio di benvenuto
print("Ciao! Benvenuto nel programma che somma i numeri che inserisci.")
print("Inserisci i numeri interi uno alla volta. Quando vuoi terminare, inserisci 0.\n")

# Inizializziamo una variabile per la somma
somma = 0

# Ciclo che continua finché l'utente non inserisce 0
while True:
    # Chiediamo all'utente di inserire un numero
    try:
        numero = int(input("Inserisci un numero intero (0 per terminare): "))
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        continue
    
    # Se l'utente inserisce 0, usciamo dal ciclo
    if numero == 0:
        break
    
    # Aggiungiamo il numero alla somma
    somma += numero
    print(f"Numero aggiunto! La somma parziale è: {somma}\n")

# Alla fine, stampiamo la somma dei numeri con un messaggio più carino
print("\n---------------------------------")
print(f"Wow, hai inserito {somma} come somma totale dei numeri!")
print("Grazie per aver giocato con i numeri! Se vuoi rifarlo, esegui di nuovo il programma.")
print("---------------------------------")
