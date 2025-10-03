list=[1,4,5]
osszeg=0
for szam in list:
	osszeg=osszeg+szam
print(f"A szamok osszege:{osszeg}")
p_szamok=[]
for szam in list:
	if szam % 2 == 0:
		p_szamok.append(szam)
	
print(f"A paros szamok {p_szamok}")