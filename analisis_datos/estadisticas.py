from typing import List, Union

# --- RETO 1: Completa la función media ---
def media(datos: List[Union[int, float]]) -> float:
    """
    Calcula el promedio de una lista de números.
    Debe lanzar un ValueError si la lista está vacía.
    """
    # 1. Valida si la lista 'datos' está vacía. Si sí, lanza ValueError.
    # TU CÓDIGO AQUÍ 
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía para calcular el promedio.")

    # 2. Retorna la suma dividida por la cantidad de elementos
    # TU CÓDIGO AQUÍ
    promedio = sum(datos) / len(datos)
    return promedio

# --- RETO 2: Completa la función mediana ---
def mediana(datos: List[Union[int, float]]) -> Union[int, float]:
    """
    Calcula el valor central de los datos.
    """
    if not datos:
        raise ValueError("Lista vacía")

    # 1. Ordena los datos (¡OJO! usa sorted() para no modificar la lista original)
    # TU CÓDIGO AQUÍ
    datos_sorted = sorted(datos)

    n = len(datos)
    mitad = n // 2

    # 2. Si n es par, devuelve el promedio de los dos del centro
    # 3. Si n es impar, devuelve el elemento central
    if n % 2 == 0:
        # TU CÓDIGO AQUÍ
        return (datos_sorted[mitad - 1] + datos_sorted{mitad}) / 2        
    else:
        # TU CÓDIGO AQUÍ
        return datos_sorted[mitad]
