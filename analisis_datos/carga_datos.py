import random
from typing import List, Tuple, Dict

def generar_lista_compras(cantidad: int = 5) -> List[Tuple[str, int]]:
    productos = {
        "manzanas": 1000, "bananos": 150, "cerezas": 2000, 
        "naranjas": 900, "pan": 2275, "leche": 840, 
        "huevos": 3400, "queso": 5000, "frijoles" : 1200
    }
    # RETO 3: Selecciona 'cantidad' productos aleatorios de la lista de items
    # Pista: Usa random.sample()
    # TU CÓDIGO AQUÍ
    cantidad = min(cantidad, len(productos))
    return random.sample(list(productos.items()), k=cantidad)

    def guardar_lista_compras(lista_compras: List[Tuple[str, int]], nombre_archivo: str):
    """
    Guarda la lista en un archivo de texto.
    Formato: producto:precio
    """
    try:
        # RETO 4: Usa 'with open(...)' para abrir el archivo en modo escritura ('w')
        # Itera sobre la lista y escribe cada línea.
        with open(nombre_archivo,"w", encoding="utf-8") as archivo
            for producto, precio in lista_compras:
                archivo.write(f"{producto}:{precio} \n")
        print(f"Archivos{nombre_archivo} guardado exitosamente!.")
        print(f"✅ Archivo guardado en {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
