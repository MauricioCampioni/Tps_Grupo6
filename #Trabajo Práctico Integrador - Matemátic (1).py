#Trabajo Práctico Integrador - Matemática/Programación I

#PARTE 1 INI (FER)##
#Definimos la funcion de pasaje a binario
def decimal_a_binario(num):

    #Si el n° es 0 hacemos
    if num == 0:
        return "0"
    
    #Si es > 0 hacemos
    num_bin = ""
    #Dividimos por 2 hasta que el cociente quede en 0
    #Mientras vamos recogiendo el resto y lo acumulamos como str para poder sumarlo al numero binario por delante sin que se realice una suma
    #ejemplo: si hago 1 + 11 arrojara 12, pero queremos ver 111
    while num > 0:
        resto = num % 2
        num_bin = str(resto) + num_bin
        num = num // 2

    #Devuelve el numero binario calculado
    return num_bin

#Definimos la funcion de pasaje a binario para numeros decimales negativos
def decimal_a_binario_negativo(num):
    
    #Definimos la cantidad de bits que queremos usar para representar el número
    bits= 8 
    
    #Obtengo el valor absoluto del número
    num = abs(num)
    
    #Calculamos el número positivo en binario
    bin_pos = decimal_a_binario(num)
#PARTE 1 FIN (FER)##    

#PARTE 2 INI ##
    #Agregamos ceros a la izquierda para completar los bits
    while len(bin_pos) < bits:
        bin_pos = "0" + bin_pos
        
    #Inverti los bits sumandole 1
    complemento_A1 = ""
    for bit in bin_pos:
        if bit == "0":
            #Se invierte 0 por 1
            complemento_A1 = complemento_A1 + "1"
        else:
            #Se invierte 1 por 0
            complemento_A1 = complemento_A1 + "0"
            
    #Le sumo 1 al complemento a1
    complemento_A2 = "" #Resultado final
    resto_suma = 1      #El 1 que le sumamos al complemento A1
    i = bits - 1        #Empieza desde el ultimo bit que esta a la derecha del todo
    
    
    while i >= 0:
        #Si hay un 1 y tambien un resto, en el resultado va un 0 y el resto queda en 1
        if complemento_A1[i] == "1" and resto_suma == 1:
            complemento_A2 = "0" + complemento_A2
            resto_suma = 1
        #Si hay un 1 y no hay resto, en el resultado va un 1 y el resto queda en 0
        elif complemento_A1[i] == "0" and resto_suma == 1:
            complemento_A2 = "1" + complemento_A2
            resto_suma = 0
        #Si no hay resto, copia el bit tal cual como estaba
        else:
            complemento_A2 = complemento_A1[i] + complemento_A2
        i -= 1 #Decrementa el contador para ir al siguiente bit a la izquierda
    #Devuelve el binario en el complemento A2    
    return complemento_A2
    
    
def es_numero(val):
    #Si el primer carácter es un signo negativo, lo ignoramos
    if val[0] == '-' and len(val) > 1:  
        val = val[1:]  #Quitamos el signo para comprobar el resto
    #Recorremos cada carácter y verificamos que todos sean dígitos
    for char in val: #Char toma un valor dentro de la cadena val y iteramos para comprobar que todos son numeros
        if char < '0' or char > '9':  #Si encontramos un carácter que no es un dígito, devolvemos False
            return False
    return True  
#PARTE 2 FIN ##

#PARTE 3 INI ##
#Definimos las funciones para convertir binario a decimal
def binario_ok (num_binario):
    #Verifica si una cadena contiene solo '0' y '1'
    for digito in num_binario:
        if digito != '0' and digito != '1':
            return False
    return True

def binario_a_decimal(num_binario):
    #Convierte un número binario a decimal 
    decimal = 0
    potencia = 0
    for digito in reversed(num_binario): #Se va iterando de derecha a izquierda y calcula las potencias de 2
        if digito == '1':
            decimal += 2**potencia
        potencia += 1 #la potencia se incrementa en cada iteración
    return decimal  #Nos devuelve el número decimal calculado

def eleccion_ok(eleccion): #validamos la entrada del usuario que sea 1 o 2
    if eleccion == '1' or eleccion == '2':
        return True
    else:
        return False
#PARTE 3 FIN ##

#PARTE 4 INI ##
#Solicitamos al usuario que elija una opcion:
eleccion = input(" Si quiere pasar de decimal a binario escriba 1, si quiere pasar de binario a decimal escriba 2: ")

while eleccion != "1" and eleccion != "2":
    
    eleccion = input("Opcion inválida. Si quiere pasar de decimal a binario escriba 1, si quiere pasar de binario a decimal escriba 2: ")

if eleccion == "1":

    numero = input("Ingrese un número: ")
    #Valido si la entrada es un número
    while es_numero(numero) == False: #Validamos si la entrada es un número
        print("Carácter incorrecto, por favor ingrese un número")  # Si no es un número, mostramos el error
        numero = input("Ingrese un número: ")

        # Convertimos la entrada en un número entero
    numero = int(numero)
#Condicional: llamamos funcion segun corresponda (entrada numero positivo o negativo)
    if numero >= 0:
        print(f"El número {numero} en binario es {decimal_a_binario(numero)}")

    else: 
        print(f"El número {numero} en binario es {decimal_a_binario_negativo(numero)}")


elif eleccion == "2":
        binario = input("Ingresa el número binario: ")

        while not binario_ok(binario): #Se valida que el número binario sea correcto, si no es correcto se vuelve a pedir
            print("Error, por favor ingresar un número binario")
            binario = input("Ingresa el número binario: ")
        
        decimal = binario_a_decimal(binario) #Se llama a la función para convertir de binario a decimal
        print(f"El número binario '{binario}' en decimal es: {decimal}")

#PARTE 4 FIN ##













