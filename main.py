cont_letra = 0
cont_palabra = 0
cont_palabras_p = 0
cadena = None
flag_p = False

while cadena !='.':
	cadena = input('Ingresar letra, termina con"."')
	cont_letra += 1
   
    #Primera letra que comienza con p. 
  if cont_letra == 1 and cadena == 'p':
    flag_p = True

	if cadena == '' or cadena == '.': # Fin de palabra

		# Se asegura que sea una palabra valida.
    if cont_letra > 1:  
			cont_palabra +=1
      # Si es una palabra valida y comienza con p. 
      if flag_p : 
        cont_palabras_p +=1
  
		cont_letra = 0

print('Cantidad de palabras:', cont_palabra )		 