import random as rdm

def ziehung(liste): 
    for i in range(1,7):
        tsize = len(liste) - i
        randomzahl = rdm.randint(0, tsize)
        liste[randomzahl], liste[tsize] = liste[tsize], liste[randomzahl]
    return liste[-6:]


def statistik(dict, gezogenenZahlen):
    for i in gezogenenZahlen:
        dict[i] += 1

def makeDict(dict):
    for i in range(1,46):
        dict[i] = 0

def main():
    lottozahlen = list(range(1,46))

    # Die 6 gezogenen Zahlen ausgeben
    resultZiehung = ziehung(lottozahlen)
    print(resultZiehung)

    # Statistik bei einem Durchlauf
    statistikDict = {}
    makeDict(statistikDict)
    statistik(statistikDict, resultZiehung)
    print(statistikDict)

    # Stastik bei 1000 10000 100000 Durchläufen:
    anzahl = [1000,10000,100000]
    for element in anzahl:
        statistikDict1 = {}
        makeDict(statistikDict1)
        for i in range(element):
            resultZiehung1 = ziehung(lottozahlen)
            statistik(statistikDict1, resultZiehung1)
        print(f"Statistiken für {element}")
        for lottozahl, zaehler in statistikDict1.items():
            print(f"{lottozahl}: {zaehler}")


if __name__ ==  "__main__":
    main()