"""Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), és írasd ki az első számjegyét!"""
print("***1. FELADAT***")
szam = int(input("Kérlek, adj meg egy számot 200 és 920 között: "))
print("A bekért szám:", szam)

while szam < 200 or szam > 920:
    print("Nem megfelelő számot adtál meg, kérlek adj meg egy helyes számot!")
    print("Kérlek adj meg egy számot 200 és 920 között: ")

elso_szamjegy = szam
while elso_szamjegy >= 10:
     elso_szamjegy //= 10

print("Az első számjegy:", elso_szamjegy)

import eljarasok

eljarasok.szamjegyek_osszege(szam)
"""Írj metódust, ami paraméterében kap két számot, és kiírja a legkisebb közös többszörösüket! Segítség: Indulj a nagyobb számtól egyesével és keresd meg azt a számot, amelyet mindkettő oszt! Meddig kell mennie a ciklusnak? """
print("***3. FELADAT***")
szam1 = int(input("Kérlek, add meg az első számot: "))
szam2 = int(input("Kérlek, add meg a második számot: "))

nagyobb_szam = szam1 if szam1 > szam2 else szam2

szamjegy = 1

while szamjegy <= szam1 * szam2:  
    if szamjegy % szam1 == 0 and szamjegy % szam2 == 0:
        print(f"A(z) {szam1} és {szam2} legkisebb közös többszöröse: {szamjegy}")
        break
    szamjegy += 1

"""Írj metódust, ami paraméterében kap két számot, és kiírja a két szám legnagyobb közös osztóját! Segítség::: A kisebbik számtól visszafelé nézzük, hogy van-e közös osztó. Nincs, ha az egyet elértük."""
print("***4. FELADAT***")
szam1 = int(input("Kérlek, add meg az első számot: "))
szam2 = int(input("Kérlek, add meg a második számot: "))


kisebb_szam = min(szam1, szam2)

while kisebb_szam > 0:
    if szam1 % kisebb_szam == 0 and szam2 % kisebb_szam == 0:
        print(f"A(z) {szam1} és {szam2} legnagyobb közös osztója: {kisebb_szam}")
        break
    kisebb_szam -= 1

