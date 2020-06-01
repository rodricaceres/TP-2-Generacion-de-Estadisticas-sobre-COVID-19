def validar(cuenta):
    pri_car = cuenta[0]
    ult_car = cuenta[len(cuenta) - 1]
    cont_arr = 0
    # No tener un sólo caracter @ en una posición intermedia de la cadena (ni la primera ni la última letra)
    # No empezar ni terminar con un punto
    if pri_car != "@" and ult_car != "@" and pri_car != '.' and ult_car != '.':
        validacion = True
    else:
        validacion = False
    # No contener dos puntos seguidos (uno a continuación del otro)
    if validacion == True:
        for caracter in cuenta:
            if caracter == "@":
                cont_arr += 1
            if cont_arr != 1:
                validacion = False       
            else:
                validacion = True    
            if caracter == "." and car == ".":
                validacion = False
                break
            car = caracter
        
    return(validacion)


cuenta = input("Ingrese cuenta en formato nombre@dominio: ")
bandera = True
cont = 0
while bandera == True:
    validacion = validar(cuenta)
    if validacion == True:
        bandera = False
        print("Validacion correcta")
    else:
        print("Validacion incorrecta")
        cuenta = input("Ingrese de nuevo la cuenta en formato nombre@dominio: ")
        cont += 1
    if cont == 3:
        print("3 Intentos fallidos")
        bandera = False