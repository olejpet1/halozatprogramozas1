nev = input("Add meg a teljes neved: ")

szavak = nev.strip().split()

monogram = ""

for szo in szavak:
    hossz = len(szo)

    betu = szo[0].upper()

    if hossz >= 3:
        a, b, c = szo[0], szo[1], szo[2]
        if (a in "Dd" and b in "Zz" and c in "Ss"):
            betu = a.upper() + b.lower() + c.lower()  
    if hossz >= 2 and betu == szo[0].upper(): 
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


    monogram += betu

print(monogram)

