import random

gondolt_szam = random.randint(1,3)

"""print(f"A gondolt szám: {gondolt_szam}")"""
bekert_szam=int(input("kérem a számot"))

if gondolt_szam == bekert_szam:
	print("Eltaláltad")
elif gondolt_szam > bekert_szam:
	print("Nagyobbra gondoltam")
else:
	print("Kisebbre gondoltam") 

#keszits egy fuggvenyt elojel neven , mely atvesz egy egesz szamot es az elojelet adja vissza

def elojel(szam):
    if szam >=0:
        return "+"
    else:
        return "-"
   
szam= int(input("Kerek egy szamot "))

print(f"A {szam} elojele:{elojel(szam)}")

def tesztesetek():
      teszt(5,"+")
      teszt(-3,"-")
      teszt(-1,"-")
      teszt(0,"+")
      teszt(1,"+")
      
def teszt(szam, elvart_elojel):
    if elojel(szam) == elvart_elojel:
            print(f"elojel({szam})=={elvart_elojel} true")
    else:
          print(f"elojel({szam})=={elvart_elojel} else")
tesztesetek()