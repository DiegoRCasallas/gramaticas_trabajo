import sys
import re

def es_valido_gramatica_g3(cadena):
    """
    Verifica si una cadena pertenece a L(G3) = {a^n b^(n+1) | n>0}
    
    Gramática:
    S → Ab
    A → aAb | ab
    
    Esto genera cadenas como: abb, aabb, aaabbb, aaaabbbb, ...
    NOTA: n>0, por lo que debe haber al menos una 'a'
    """
    # Verificar que no esté vacía
    if len(cadena) == 0:
        return False
    
    # Verificar que solo contenga 'a' y 'b', y que tenga al menos una 'a'
    if not re.match(r'^a+b+$', cadena):
        return False
    
    # Contar número de 'a's y 'b's
    num_a = cadena.count('a')
    num_b = cadena.count('b')
    
    # Para L(G3): número de b's debe ser exactamente n+1 donde n es número de a's
    # y n > 0 (debe haber al menos una 'a')
    return num_a > 0 and num_b == num_a + 1

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de texto línea por línea.
    Para cada línea, verifica si cumple con la gramática G3.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                # Remover espacios en blanco y saltos de línea
                patron = linea.strip()
                
                # Procesar incluso líneas vacías (las evaluamos como NO ACEPTA)
                if es_valido_gramatica_g3(patron):
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
    """
    Función principal del programa.
    Espera recibir el nombre del archivo como argumento de línea de comandos.
    """
    # Verificar que se proporcione exactamente un argumento (el nombre del archivo)
    if len(sys.argv) != 2:
        print("Uso: python programa.py archivo.txt")
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    
    # Verificar que el archivo tenga extensión .txt
    if not nombre_archivo.endswith('.txt'):
        print("Error: El archivo debe tener extensión .txt")
        sys.exit(1)
    
    # Procesar el archivo
    procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()