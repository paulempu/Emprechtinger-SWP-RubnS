import random

def GetFarbe(kartennummer):
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

def GetSymbol(kartennummer):
        symbole = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bube", "Dame", "König", "Ass"]
        if kartennummer >= 0 and kartennummer <= 51:
            return symbole[kartennummer % 13]
        return None

def Ziehung(liste):
    for i in range(1, 6):
        tlength = len(liste) - i
        rzahl = random.randint(0, tlength)
        liste[rzahl], liste[tlength] = liste[tlength], liste[rzahl]
    return liste[-5:]

def main():
    # 0-12: herz   13-25: karo   26-38: pik   39-51: kreuz
    karten = [k for k in range(52)]

    testliste = Ziehung(karten)
    print(testliste)

    for i in testliste:
        print(GetFarbe(i), GetSymbol(i))




if __name__ == "__main__":
    main()