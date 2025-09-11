# feladat: négyzet/téglalap kerületének számítása
def beker(alakzat, oldal):
    """Bekéri az 'alakzat' 'oldal' oldalának hosszat"""
    oldalhossz = int(input(f"Kérem a {alakzat} {oldal} oldalanak hosszat [cm]: "))
    return oldalhossz

def teglalapKerulete(a, b):
    """ kiszamolja az 'a' és 'b' oldal ismeretében a teglalap kerületet. K= 2*(a+b)"""
    kerulet = 2 * (a + b)
    return kerulet

def kiir(alakzat, kerulet):
    """Kiírja az 'alakzat' 'kerulet'-et """
    print(f"A {alakzat} kerülete: {kerulet}cm.")

# input
mit = input("[T]églalap vagy [N]égyzet kerületet számoljam [T|N]?") 
if mit.upper() == "N":
    alap = beker("négyzet", "a")
    # calculation
  
    kerulet = teglalapKerulete(alap, alap)
   
    # output
  
    kiir("négyzet", kerulet)
elif mit.upper() == "T":
    a_oldal = beker("téglalap","a")
    b_oldal = beker("téglalap","b")
   
    # calculation
    
    kerulet = teglalapKerulete(a_oldal, b_oldal)
   
    # output
   
    kiir("teglalap", kerulet)
else:
    print("Hibás választás. Kilépek!")
