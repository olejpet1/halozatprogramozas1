# A róka libát lop a faluból, a hét minden napján egyet. Ezek súlyát tároltuk el a libak.txt-ben. A farkas várja a falu határában a rókát és a 3 kg-nál nehezebb libát elveszi, a kisebbeket meghagyja a rókánál.
libak=[]
with open("libak.txt")as fin:
	for suly in fin:
		libak.append(int(suly.strip()))
print(libak)

# 1. Hány kiló libát evett a róka a héten?
roka_kilo=0
for liba in libak:
	if liba <=3:
		roka_kilo=roka_kilo+liba
print(f"kg libat {roka_kilo}")
# 2. Átlagosan hány kilósak a rókánál maradt libák?
roka_darab = 0
for liba in libak:
	if liba <= 3:
		roka_darab = roka_darab + 1
print(f"átlagosan {roka_kilo/roka_darab}")
# 3. Előfordult-e, hogy a róka legalább 3kg-os libát lopott?
#Eldőntés
volt_legalabb_harom=False
for liba in libak:
	if liba>=3:
		volt_legalabb_harom=True
		break
if volt_legalabb_harom:
	print("volt")
else:
	print("nem")
# 4. Előfordult-e, hogy a róka kisebb libát lopott, mint az előző napon?
volt_kisebb=False
for index in range(len(libak)-1):
	if libak[index]>libak[index+1]:
		volt_kisebb=True
		break
if volt_kisebb:
	print("Előfordult, hogy a róka kisebb libát lopott, mint az előző napon")
else:
	print("Nem előfordult hogy a róka kisebb libát lopott, mint az előző napon?")
# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
# 7. Hány liba jutott a héten a farkasnak?
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?




