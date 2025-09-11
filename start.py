# feladat: négyzet/téglalap kerületének számítása
def beker(alakzat, oldal):
    """Bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    oldalhossz = int(input(f"Kérem a {alakzat} {oldal} oldalának hosszát [cm]: "))
    return oldalhossz

def teglalapKerulete(a, b):
    """ kiszámolja az 'a' és 'b' oldal ismeretében a téglalap kerületét. K= 2*(a+b)"""
    kerulet = 2 * (a + b)
    return kerulet

def kiir(alakzat, kerulet):
    """Kiírja az 'alakzat' 'kerulet'-ét """
    print(f"A {alakzat} kerülete: {kerulet}cm.")

# input
mit = input("[T]églalap vagy [N]égyzet kerületét számoljam [T|N]?") 
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
