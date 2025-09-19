lista = [2,4,1,8,3]
#1
ossze=0
for i in lista:
	ossze+= i
print(f"A lista elemeinek ossege:{ossze}")
#b1 lsita elemeinek darabszama
darab=0
for szam in lista:
	darab+=1
print(f"a szamok darabszama : {darab}")

#A 2. paros szamok atlaga
paros_osszeg=0
paros_db=0
for szam in lista:
	if szam % 2 ==0:
		paros_osszeg+=szam
		paros_db+=1 

print(f"A szamok atlaga: {paros_osszeg/paros_db:.3f}")


#b2 paros szamok darabszamok
print(f"A b2 paros szamok darabszama: {paros_db}")

# A 2 es b2 
parosoklista=[szam for szam in lista if szam % 2 == 0 ]
#parosok lista = [2,4,8]
print(f"A szamok atlaga: {sum(parosoklista)/len(parosoklista):.3f}")
print(f"B.2 paros szamok darab szama: {len(parosoklista)}")


#mindenkie 
for szam in lista:
	print(szam, "*" *szam)