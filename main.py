cont_letra = 0
cont_palabra = 0
cont_palabras_p = 0
cont_ta = 0
cadena = None
primer_caracter = False

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


		if cadena == 't' and primer_caracter == False
			primer_caracter = True
		if cadena == 'a' and primer_caracter == True
			cont_ta +=1	
			primer_caracter = False


print('Cantidad de palabras:', cont_palabra )		
print('Cantidad de palabras que inician con p:', cont_palabras_p )	 

c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".