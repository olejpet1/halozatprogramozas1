# Bekérjük a nevet
nev = input("Add meg a teljes neved: ")

# Szavakra bontás szóköz szerint
szavak = nev.strip().split()

# Üres monogram
monogram = ""

# Végigmegyünk a szavakon
for szo in szavak:
    hossz = len(szo)

    # Alapértelmezett betű: az első karakter nagybetűsen
    betu = szo[0].upper()

    # Ha legalább 3 karakter van a szóban, megnézzük az első 3 betű kombinációját
    if hossz >= 3:
        a, b, c = szo[0], szo[1], szo[2]
        if (a in "Dd" and b in "Zz" and c in "Ss"):
            betu = a.upper() + b.lower() + c.lower()  # pl. "Dzs"
    # Ha nem Dzs, de van legalább 2 karakter, akkor megnézzük a 2 betűs magyar betűket
    if hossz >= 2 and betu == szo[0].upper():  # csak akkor nézzük, ha nem volt Dzs
        a, b = szo[0], szo[1]
        if (
            (a in "Cc" and b in "Ss") or
            (a in "Dd" and b in "Zz") or
            (a in "Gg" and b in "Yy") or
            (a in "Ll" and b in "Yy") or
            (a in "Nn" and b in "Yy") or
            (a in "Ss" and b in "Zz") or
            (a in "Tt" and b in "Yy") or
            (a in "Zz" and b in "Ss")
        ):
            betu = a.upper() + b.lower()

    # Monogramhoz hozzáadjuk
    monogram += betu

# Kiírjuk az eredményt
print(monogram)

