lista=[1,1,2,2,4,5,2,1,3]
egyes_db=0
kettes_db=0
harmas_db=0
negyes_db=0
otos_db=0

for szam in lista:
	if szam==1:
		egyes_db+=1
	elif szam==2:
		kettes_db+=1
	elif szam==3:
		harmas_db+=1
	elif szam==4:
		negyes_db+=1
	elif szam==5:
		otos_db+=1
print(f"Az 1-es szambol ennyi db van {egyes_db}")
print(f"Az 1-es szambol ennyi db van {kettes_db}")
print(f"Az 1-es szambol ennyi db van {harmas_db}")
print(f"Az 1-es szambol ennyi db van {negyes_db}")
print(f"Az 1-es szambol ennyi db van {otos_db}")


db=lista.count(1)
db2=lista.count(2)
db3=lista.count(3)
db4=lista.count(4)
db5=lista.count(5)
print(db,db2,db3,db4,db5)


for i in range(1,6):
	print(f"{i} bol van {lista.count(i)}")