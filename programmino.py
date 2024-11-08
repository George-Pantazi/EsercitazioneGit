# Inizializza la variabile per la somma
somma = 0

# Continua a chiedere numeri finché non viene inserito lo zero
while True:
    numero = int(input("Inserisci un numero intero"))
    
    # Se l'utente inserisce 0, esci dal ciclo
    if numero == 0:
        break
    
    # Aggiungi il numero alla somma
    somma += numero

# Stampa la somma totale
print("La somma di tutti i numeri inseriti è:", somma)
