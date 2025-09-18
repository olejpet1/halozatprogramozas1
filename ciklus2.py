# Kérjünk be számokat és adjuk meg az összegüket
# 1 0 végjelig
# 2 Enter végjelig HF
osszeg=0
be_n=1
while be_n !=0:
    be_n=int(input("kérek egy számot: "))
    osszeg+=be_n

print(osszeg)


osszeg = 0
be = "0"   # nem üres, hogy belépjen a ciklusba

while be != "":
    be = input("Kérek egy számot (Enter a vége): ")
    if be != "":          # csak akkor adja hozzá, ha tényleg számot írtunk be
        osszeg += int(be)

print("Az összeg:", osszeg)

