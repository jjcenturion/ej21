cont_letra = 0
cont_palabra = 0
cont_palabras_p = 0
cadena = None

while cadena !='.':
	cadena = input('Ingresar letra, termina con"."')
	cont_letra += 1

	if cadena == ' ' or cadena == '.': # Fin de palabra

		# Se asegura que sea una palabra valida.
		if cont_letra > 1:  
			cont_palabra +=1
     
		cont_letra = 0
  # Si no es el fin de la palabra
	else:  
     #Primera letra que comienza con p. 
		if cont_letra == 1 and cadena == 'p':
			cont_palabras_p +=1

print('Cantidad de palabras:', cont_palabra )		
print('Cantidad de palabras que inician con p:', cont_palabras_p )	 