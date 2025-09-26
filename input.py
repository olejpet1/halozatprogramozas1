osszeg=0
be_n=1
while be_n !=0:
    be_n=int(input("kérek egy számot: "))
    osszeg+=be_n

print(osszeg)

#hazi 

osszeg = 0
be = "0" 

while be != "":
    be = input("Kérek egy számot: ")
    if be != "":      
        osszeg += int(be)

print("Az összeg:", osszeg)


#orai feladat
ossz=0
while True:
    beszam=int(input("kérek egy számot"))
    if beszam!=0:
        ossz=ossz+beszam
    else:
        break
print(f"Ez a szamok osszege: {ossz}")

#kerjel be egy szamot 0 tol eddig a paros szamokat irasd ki
szam=int(input(f"kerem a hatar szamot"))
szam1=0
while szam1!=szam+1:
    print(szam1)
    szam1+=1
    if szam1%2==0

	