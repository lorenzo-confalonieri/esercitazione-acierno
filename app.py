# Dizionario contenente parole chiave con punteggi associati.
# Le parole chiave sono divise in due categorie: "sospettoso" e "tranquilla".
# Ogni parola ha un punteggio positivo o negativo che contribuisce alla valutazione del titolo.
keywords = {
    "sospettoso": {
        "scandalo": -3,  # Parola con punteggio negativo (sospettosa).
        "shock": -3,
        "incredibile": -2,
        "clamoroso": -2,
        "allarme": -3,
        "segreto": -2,
        "bufala": -3,
        "truffa": -3,
        "cospirazione": -2,
        "manipolazione": -2
    },
    "tranquilla": {
        "ufficiale": 3,  # Parola con punteggio positivo (tranquilla).
        "confermato": 3,
        "studio": 2,
        "ricerca": 2,
        "esperto": 2,
        "scientifico": 3,
        "verificato": 3,
        "fonte": 2,
        "autorizzato": 3,
        "approvato": 3
    }
}

# Funzione che calcola il punteggio di un titolo in base alle parole chiave.
def punteggio(titolo):
    punteggio = 0  # Inizializza il punteggio a 0.
    parole = titolo.lower().split()  # Converte il titolo in minuscolo e lo divide in parole.
    for parola in parole:  # Itera su ogni parola del titolo.
        if parola in keywords["sospettoso"]:  # Controlla se la parola è "sospettosa".
            punteggio += keywords["sospettoso"][parola]  # Aggiunge il punteggio negativo.
        elif parola in keywords["tranquilla"]:  # Controlla se la parola è "tranquilla".
            punteggio += keywords["tranquilla"][parola]  # Aggiunge il punteggio positivo.
    return punteggio  # Restituisce il punteggio totale.

# Funzione che classifica una notizia in base al punteggio calcolato.
def notizia(punteggio):
    if punteggio < -5:  # Se il punteggio è inferiore a -5, la notizia è "Fake".
        return "Fake"
    elif punteggio <= 2:  # Se il punteggio è compreso tra -5 e 2, la notizia è "Dubbia".
        return "Dubbia"
    else:  # Se il punteggio è maggiore di 2, la notizia è "Affidabile".
        return "Affidabile"

# Richiede all'utente di inserire titoli separati da una virgola.
titoli = input("Inserisci i titoli separati da una virgola: ").split(',')

# Itera su ogni titolo inserito dall'utente.
for titolo in titoli:  # Itera sulla lista di titoli.
    punteggio2 = punteggio(titolo.strip())  # Calcola il punteggio del titolo, rimuovendo eventuali spazi.
    print("Titolo:", titolo.strip())  # Stampa il titolo.
    print("Punteggio:", punteggio2)  # Stampa il punteggio calcolato.
    print("Classificazione:", notizia(punteggio2))  # Stampa la classificazione del titolo.
    print("-" * 30)  # Stampa una linea di separazione.

