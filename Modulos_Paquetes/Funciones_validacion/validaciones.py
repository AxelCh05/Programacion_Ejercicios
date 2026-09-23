from Funciones.Funcion_interna.nota_validada import mostrar_mensaje

def validar_nota(nota:int, contador:int)->int:
    """ Valida que la nota esté en el rango de 1 a 10.
    Args:
        nota (int): nota del alumno en entero
        contador (int): cuenta la cantidad de notas

    Returns:
        int: retorna la nota validada.
    """
    while nota < 1 or nota > 10:
        print(f"ERROR. Nota fuera de rango.")
        nota = int(input(f"Ingresar la nota {contador}"))
    mostrar_mensaje("LA NOTA HA SIDO VALIDADA.")
    return nota