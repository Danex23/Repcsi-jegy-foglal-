import random
helyek =[[["A","B","C","D","E","F"],["5","6","7","8","9","10","11"]],
        [["A","B","C","D","E","F"],["1","2","3","4"]]
        ]
foglalt  = []
busfoglalt = []
foglalas = []
#Osztály szerinti szűrés
#66 hely van
def utasok ():
    oszlop = ''
    for x in range(random.randint(10,50)):
        oszlop = random.choice(helyek[0][0])
        sor = random.choice(helyek[0][1])
        foglalt.append(oszlop+sor)
    for x in range(random.randint(5,15)):
        oszlop = random.choice(helyek[1][0])
        sor = random.choice(helyek[1][1])
        busfoglalt.append(oszlop+sor)
aktualis_ules = None
aktualis_sor = None
aktualis_oszlop = None
random_oszlop = None
random_sor = None

tipus = input("Random jegy vagy választasz?(r ha igen): ")
ablak = input("Szeretnél ablak mellet ülni? +100$-ért?(i/n): ")
szam = int(input("Hány főre szeretne foglalni? "))
if szam >= 16:
    print("Nem foglalhatsz többet mint 10!")
    szam  = 10
utasok()
for i in range(szam):
    if tipus == "R" or tipus == "r":
        if ablak == "i" or ablak == "I":
            siker = False
            for i in range(1000):
                random_oszlop = random.choice(helyek[0][0])
                random_sor = random.choice(helyek[0][1])
                if siker == False:
                    if random_oszlop == "A" or random_oszlop == "F":
                        if aktualis_ules not in foglalt:
                            aktualis_ules = random_oszlop + random_sor
                            foglalt.append(aktualis_ules)
                            foglalas.append(aktualis_ules)
                            siker = True
            if siker == False:
                print("Nem sikerült foglalni keresünk máshol!")   
                while True:
                    random_oszlop = random.choice(helyek[0][0])
                    random_sor = random.choice(helyek[0][1])
                    aktualis_ules = random_oszlop + random_sor
                    if aktualis_ules not in foglalt:
                        foglalt.append(aktualis_ules)
                        foglalas.append(aktualis_ules)
                        break
        else:
            while True:
                random_oszlop = random.choice(helyek[0][0])
                random_sor = random.choice(helyek[0][1])
                aktualis_ules = random_oszlop + random_sor
                if aktualis_ules not in foglalt:
                    foglalt.append(aktualis_ules)
                    foglalas.append(aktualis_ules)
                    break
    else:
        osztály = input("Milyen osztályon szeretnél utazni?: ")
        if osztály == "Economy" or osztály == "economy" or osztály == "E" or osztály == "e":
            aktualis_oszlop = input("Melyik oszlopban szeretne ülni? (A-F) ")
            while True:
                aktualis_sor = input("Meylik sorban szeretne ülni? (Túrista osztályon van! Csak 5. és utána lévő sorokat választhat!)" )
                if aktualis_sor >= 5:
                    aktualis_ules = aktualis_oszlop + aktualis_sor
                    if aktualis_ules not in foglalt:
                        foglalt.append(aktualis_ules)
                        foglalas.append(aktualis_ules)
                        break
        if osztály == "Busniess" or osztály == "busniess" or osztály == "B" or osztály == "b":
            aktualis_oszlop = input("Melyik oszlopban szeretne ülni? (A-F) ")
            while True:
                aktualis_sor = input("Meylik sorban szeretne ülni? (Túrista osztályon van! 1-4 ig választhat)" )
                if aktualis_sor < 5:
                    aktualis_ules = aktualis_oszlop + aktualis_sor
                    if aktualis_ules not in foglalt:
                        foglalt.append(aktualis_ules)
                        foglalas.append(aktualis_ules)
                        break
#test
print(foglalas)