import sys

def es_valido_gramatica_g4(cadena):
    """
    Verifica si una cadena pertenece a L(G4) = {abb, ab}
    Gramática:
    S → A b
    A → ab | a
    """
    return cadena in ("abb", "ab")

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de texto línea por línea.
    Para cada línea, verifica si cumple con la gramática G4.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                patron = linea.strip()
                if es_valido_gramatica_g4(patron):
                    print("ACEPTO")
                else:
                    print("NO ACEPTA")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Uso: python programa.py archivo.txt")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    
    if not nombre_archivo.endswith('.txt'):
        print("Error: El archivo debe tener extensión .txt")
        sys.exit(1)
    
    procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()
