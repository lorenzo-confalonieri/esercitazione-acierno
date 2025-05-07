
keywords = {
    "sospettoso": {
        "scandalo": -3,
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
        "ufficiale": 3,
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

def punteggio(titolo):
    punteggio = 0
    parole = titolo.lower().split()
    for parola in parole:
        if parola in keywords["sospettoso"]:
            punteggio += keywords["sospettoso"][parola]
        elif parola in keywords["tranquilla"]:
            punteggio += keywords["tranquilla"][parola]
    return punteggio

def notizia(punteggio):
    if punteggio < -5:
        return "Fake"
    elif punteggio <= 2:
        return "Dubbia"
    else:
        return "Affidabile"


def main():
    titoli = input("Inserisci i titoli separati da una virgola: ").split(",")
    for titolo in titoli:
        punteggio = punteggio(titolo)
        print("Titolo:", titolo.strip())
        print("Punteggio:", punteggio)
        print("Classificazione:", notizia(punteggio))
        print("-" * 30)

