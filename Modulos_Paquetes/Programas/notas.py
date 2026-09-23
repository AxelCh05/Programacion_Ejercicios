from Funciones_validacion.validaciones import validar_nota


def notas()-> None: 
    #TEMA: 
    #1. CONTADORES
    #2. ACUMULADORES
    #3. PROMEDIOS. 
    #4. MAXIMOS Y MINIMOS.

    #PROGRAMA COORDINACIÓN ACADEMICA UTN FRA.
    #Inicialimos algunas variables.
    cantidad_notas = 6 #porque no sabemos cuantas son.
    contador = 0 #NUESTRO CONTADOR.
    acumulador = 0 #NUESTRO ACUMULADOR.
    maximo = 0 #valor máximo.
    minimo = 11 #valor mínimo.
    contador2=0 #Contador APD

    print(f'BIENVENIDO A UTN \n SISTEMA DE NOTAS CONSOLACAD')
    #usuario = input(f'Usuario: ')
    #contrasena = input(f'Contrasena: ')

    #--------
    #AQUI VALIDARIAMOS USUARIO Y CONTRASEÑA. 
    #--------

    #print(f'Bienvenido {usuario}') 

    #Solicitamos nombre del estudiante. 
    #nombre = input(f'Ingresá el nombre: ')
    #Solicitamos notas. Usamos un otro while para ello. 
    print(f'{contador}')

    for contador in range(cantidad_notas, 0, -1):
    #for contador in range(cantidad_notas):
    #while contador < cantiadad_notas: 
        #Aquí el cargado de notas. SOLO LAS MOSTRAREMOS EN PANTALLA. 
        #Cuando el for es en aumento, colocar contador+1.
        nota = input(f'ingresar la nota {contador}: ')
        
        #----------------
        #VALIDA LA CADENA DE CARACTERES SI ES UN NUMERO, usar int() para entero. 
        #Condicional de True.
        #----------------
        nota = int(nota)
        #validamos nota
        nota = validar_nota(nota, contador)
            
        #Cuando el for es en aumento, colocar contador+1.
        print(f'{contador}. {nota}')
        #Acumulamos la nota: 
        acumulador += nota #acumular = acumulador + nota 
        
        #SI TENEMOS TRES NOTAS >= 6, romprer el programa.
        if nota >= 6: 
            contador2 += 1


        if contador2 == 3: 
            break 

        #VARIFICAR MAXIMOS Y MINIMOS 
        if nota > maximo: 
            maximo = nota
        elif nota < minimo: 
            minimo = nota
        #else: 
        #    print(f'no se encontró ninguno nuevo.')

        if contador2 < 3: 
            continue

        print('SEGUIMOS')


        #contador += 1

    #PROMEDIOS.
    promedio = acumulador / cantidad_notas

    #CALCULAR EL PROMEDIO DE 3. 

    #PRESENTAMOS EN PANTALLA LOS RESULTADOS.
    print(f'RESULTADOS DE LA CARGA DE NOTAS: \n\tCONTADOR: {contador} \n\tACUMULADOR: {acumulador} \n\tPROMEDIO: {promedio} \n\tNOTA MÁXIMA: {maximo} \n\tNOTA Mínima: {minimo}')

