lista = [1,2,3,4,5]

def osszegez(lista):
	osszeg=0
	for elem in lista:
		osszeg +=elem
	return osszeg
print(f"lista elemeinek osszege: {osszegez(lista)}")
def paros(lista):
	darab = 0 
	for elem in lista:
		if elem % 2 == 0:
			darab += 1 
	return darab


print(f"A lista paris elemeinek osszege {paros(lista)}")