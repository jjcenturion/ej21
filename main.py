cont_letra = 0
cont_palabra = 0
cadena = None

while cadena !='.':
	cadena = input('Ingresar letra, termina con"."')
	cont_letra += 1

	if cadena == '' or cadena == '.':
		if cont_letra > 1:
			cont_palabra +=1
  
		cont_letra = 0

print('Cantidad de palabras:', cont_palabra )		