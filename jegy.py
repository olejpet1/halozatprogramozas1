spec_betuk = ["Dzs", "Cs", "Dz", "Gy", "Ly", "Ny", "Sz", "Ty", "Zs"]

nev = input("Add meg a teljes neved: ")

szavak = nev.strip().split()

monogram = ""

for szo in szavak:
    if len(szo) >= 3 and (szo[0].upper() + szo[1].lower() + szo[2].lower()) in spec_betuk:
        monogram += szo[0].upper() + szo[1].lower() + szo[2].lower()
    elif len(szo) >= 2 and (szo[0].upper() + szo[1].lower()) in spec_betuk:
        monogram += szo[0].upper() + szo[1].lower()
    else:
        monogram += szo[0].upper()
print("A monogramod:", monogram)

# OLEJ PETER SZOMBAT ALEX 
