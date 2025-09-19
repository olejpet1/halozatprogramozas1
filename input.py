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

all=0
while True:
    bestring=input("Kérek egy számot")
	if bestring !="":
        all=all+int(bestring)
    else:
        break
print(f"Ez a szamok osszege: {all}")
	