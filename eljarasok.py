def szamjegyek_osszege(szam):
    """Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. 
PL. 324 -> „324 számjegyeinek összege: 9” """
    print("***2. FELADAT***")
    szamjegy_osszeg = 0
    eredeti_szam = szam
    
    while szam > 0:
        szamjegy = szam % 10
        szamjegy_osszeg += szamjegy
        szam //= 10

    print(f"{eredeti_szam} számjegyeinek összege: {szamjegy_osszeg}")


