szamok=[1,1,2,2,4,5,2,1,3]
# egyes_db=0
# kettes_db=0
# harmas_db=0
# negyes_db=0
# otos_db=0

# for szam in szamok:
# 	if szam==1:
# 		egyes_db+=1
# 	elif szam==2:
# 		kettes_db+=1
# 	elif szam==3:
# 		harmas_db+=1
# 	elif szam==4:
# 		negyes_db+=1
# 	elif szam==5:
# 		otos_db+=1
# print(f"Az 1-es szambol ennyi db van {egyes_db}")
# print(f"Az 1-es szambol ennyi db van {kettes_db}")
# print(f"Az 1-es szambol ennyi db van {harmas_db}")
# print(f"Az 1-es szambol ennyi db van {negyes_db}")
# print(f"Az 1-es szambol ennyi db van {otos_db}")


# db=szamok.count(1)
# db2=szamok.count(2)
# db3=szamok.count(3)
# db4=szamok.count(4)
# db5=szamok.count(5)
# print(db,db2,db3,db4,db5)


# for i in range(1,6):
# 	print(f"{i} bol van {szamok.count(i)}")
darab=[0,0,0,0,0]
for szam in szamok:
	darab[szam-1]+=1
print(darab)

for i in range(len(darab)):
	print(f"{i+1}-bol van {darab[i]}")