import sys
import re

def es_valido_gramatica_g2(cadena):
    """
    Verifica si una cadena pertenece a L(G2) = {a^n b^(n+1) | n>=0}
    
    Gramática:
    S → Ab
    A → aAb | ε
    
    Esto genera cadenas como: b, abb, aabb, aaabbb, aaaabbbb, ...
    """
    # Verificar que no esté vacía
    if len(cadena) == 0:
        return False
    
    # Verificar que solo contenga 'a' y 'b'
    if not re.match(r'^a*b+$', cadena):
        return False
    
    # Contar número de 'a's y 'b's
    num_a = cadena.count('a')
    num_b = cadena.count('b')
    
    # Para L(G2): número de b's debe ser exactamente n+1 donde n es número de a's
    # Es decir: num_b = num_a + 1
    return num_b == num_a + 1

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de texto línea por línea.
    Para cada línea, verifica si cumple con la gramática G2.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                # Remover espacios en blanco y saltos de línea
                patron = linea.strip()
                
                # Saltar líneas vacías
                if not patron:
                    continue
                
                # Verificar si el patrón es aceptado por la gramática
                if es_valido_gramatica_g2(patron):
                    print("ACEPTO")
                else:
                    print("NO ACEPTA")
                    
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
        return False
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return False
    
    return True

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