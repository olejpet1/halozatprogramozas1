#feladat: negyzet/teglalap keuletenek szamitasa
def beker(alakzat, oldal):
	"""""Bekéri az 'alakzat' 'oldal' oldalanak hosszat"""
	oldalhossz = int(input("Kérem a {alakzat} {oldal} oldalanak hosszat [cm]:"))
	return oldalhossz
#def	teglalapKerulete(a, b)
#	"""kiszamolja az 'a' es 'b' oldal ismereteben a teglalap keruletet K=2*(a+b)"""
	kerulet = 2* (a+b)
def kiir(alakzat, kerulet):

#input  m = input("[T]églalap vagy [N]égyzet keruletet szamoljam? [T|N]")
#if mit.upper() == "N":
	alap = beker("négyzet", "a")
	#calculation
	kerulet = teglalapKerulete(alap, alap)
	#output 
	print(f"A negyzet kerulete: {kerulet}cm. ")
#elif mit.upper() == "T" :
	a_oldal = beker("téglalap" , "a")
	b_oldal = beker("téglalap" , "b")
	#calculation
	kerulet = teglalapKerulete(a_oldal, b_oldal )
	#output 
	print(f"A negyzet kerulete: {kerulet}cm. ")
#else:
	print("Hibá választás. Kilépek")