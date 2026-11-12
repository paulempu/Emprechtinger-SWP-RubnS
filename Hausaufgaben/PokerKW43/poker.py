import random

def getFarbe(kartennummer):
        indiz = kartennummer // 13
        match indiz:
            case 0: 
                return "herz"
            case 1:
                return "karo"
            case 2:
                return "pik"
            case 3:
                return "kreuz"
        return 

def getSymbol(kartennummer):
        symbole = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bube", "Dame", "König", "Ass"]
        if kartennummer >= 0 and kartennummer <= 51:
            return symbole[kartennummer % 13]
        return None

def ziehung(liste):
    for i in range(1, 6):
        tlength = len(liste) - i
        rzahl = random.randint(0, tlength)
        liste[rzahl], liste[tlength] = liste[tlength], liste[rzahl]
    return liste[-5:]

def zaehleWerte(hand):
    zaehler = {}
    for karte in hand:
        wert = karte % 13
        if wert in zaehler:
            zaehler[wert] += 1
        else:
            zaehler[wert] = 1
    return zaehler

def istFlush(hand):
    farben = [karte // 13 for karte in hand]
    if len(set(farben)) == 1:
        return True
    return False

def istStrasse(hand):
    werte = sorted(karte % 13 for karte in hand)
    if werte == [0, 1, 2, 3, 12]:
        return True
    if len(set(werte)) == 5:
        if werte[4] - werte[0] == 4:
            return True
    return False

def getKombination(hand):
    haeufigkeiten = sorted(zaehleWerte(hand).values())
    flush = istFlush(hand)
    strasse = istStrasse(hand)
    if flush and strasse:
        return "Straight Flush"
    if haeufigkeiten == [1, 4]:
        return "Vierling"
    if haeufigkeiten == [2, 3]:
        return "Full House"
    if flush:
        return "Flush"
    if strasse:
        return "Straße"
    if haeufigkeiten == [1, 1, 3]:
        return "Drilling"
    if haeufigkeiten == [1, 2, 2]:
        return "Zwei Paare"
    if haeufigkeiten == [1, 1, 1, 2]:
        return "Paar"
    return "Nichts"

def main():
    # 0-12: herz   13-25: karo   26-38: pik   39-51: kreuz
    karten = [k for k in range(52)]

    # eine Beispielhand
    hand = ziehung(karten)
    for karte in hand:
        print(getFarbe(karte), getSymbol(karte))
    print(getKombination(hand))
    print()

    # Statistik
    anzahl = 100000
    statistik = {"Nichts": 0, "Paar": 0, "Zwei Paare": 0, "Drilling": 0, "Straße": 0, "Flush": 0, "Full House": 0, "Vierling": 0, "Straight Flush": 0}
    echt = {"Nichts": 50.12, "Paar": 42.26, "Zwei Paare": 4.75, "Drilling": 2.11, "Straße": 0.39, "Flush": 0.20, "Full House": 0.14, "Vierling": 0.02, "Straight Flush": 0.0015}

    for i in range(anzahl):
        hand = ziehung(karten)
        kombination = getKombination(hand)
        statistik[kombination] += 1

    print(f"Statistik für {anzahl} Spiele")
    for kombination, zaehler in statistik.items():
        prozent = zaehler / anzahl * 100
        print(f"{kombination}: {zaehler} = {prozent:.2f} % (echt: {echt[kombination]} %)")

    




if __name__ == "__main__":
    main()