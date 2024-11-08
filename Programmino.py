# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:27:14 2024

@author: net
"""

# Chiediamo il nome e l'età dell'utente
nome = input("Qual è il tuo nome? ")
eta = int(input("Quanti anni hai? "))

# Calcoliamo l'anno in cui l'utente compirà 100 anni
anno_corrente = 2024
anno_100 = anno_corrente + (100 - eta)

# Mostriamo il risultato
print(f"Ciao {nome}, compirai 100 anni nel {anno_100}.")
