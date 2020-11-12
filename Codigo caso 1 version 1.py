#programa para procesar la posibilidad de votar

#subproceso para calcular mayoria de edad

def mayoria_Edad (año,mes):

    if (año<2002):

        mayor_edad="si"

    else:
        if (año==2020 and mes<9):

            mayor_edad="si"
        else:

            mayor_edad="no"

    return mayor_edad

#proceso principal

def principal ():
    
    for cont in range (50):

        nombre=input("Ingrese su nombre: ")
        año_nacimiento= int(input("Ingrese su año de nacimiento: "))
        mes_nacimiento= int(input("Ingrese su mes de nacimiento (en número): "))
        
        

        mayor_edad=mayoria_Edad(año_nacimiento,mes_nacimiento)

        if (mayor_edad=="si"):
            solicitud_exp= input("¿Ya solicitó la expedición de su cédula (si/no): ")
        
            if (solicitud_exp=="si"):
               documento=input("¿Ya tiene su documento? (si/no): ")
               if (documento=="si"):
                   habilitado_votar="si"
               else:
                   habilitado_votar = "no"
            else:
                habilitado_votar="no"
            
        else:
            habilitado_votar = "no"
            
                 
        
        print (nombre)
        print ("Habilitado a votar: ", habilitado_votar)
        
#llamado a principal

principal ()



    

    
    
    
    
    
    
                
                            
