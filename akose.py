nevek=["Tibi","Évi","Sanyi","Karcsi","Lili"]
nemek=[1,2,1,1,2]

#1.Hany fiu van?
#2.Fiú nevei:
#3.Hány % a fiuk aranya
for i in range(len(nevek)):
	print(nevek[i])
fiunevek=[]
for i in range(len(nevek)):
	if nemek[i]== 1:
		fiunevek.append(nevek[i])
print(fiunevek)
print(len(fiunevek))
print(f"{len(fiunevek)/len(nevek)*100}% a fiuk aranya.")