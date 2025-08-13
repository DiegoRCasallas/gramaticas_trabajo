import sys
import os

def es_palindromo_binario(cadena):
    """
    Verifica si una cadena es un palíndromo binario válido.
    La gramática acepta: S → 0S0 | 1S1 | 0 | 1
    Esto genera palíndromos de 0s y 1s.
    """
    # Verificar que solo contenga 0s y 1s
    if not all(c in '01' for c in cadena):
        return False
    
    # Verificar que no esté vacía
    if len(cadena) == 0:
        return False
    
    # Verificar si es palíndromo
    return cadena == cadena[::-1]

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de texto línea por línea.
    Para cada línea, verifica si cumple con la gramática.
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
                if es_palindromo_binario(patron):
                    print(f"Línea {numero_linea}: '{patron}' -> ACEPTO")
                else:
                    print(f"Línea {numero_linea}: '{patron}' -> NO ACEPTA")
                    
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
        return False
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return False
    
    return True

def validar_cadena_individual(cadena):
    """
    Valida una cadena individual y muestra el resultado.
    """
    if es_palindromo_binario(cadena):
        print("ACEPTO")
    else:
        print("NO ACEPTA")

def main():
    """
    Función principal del programa.
    """
    print("=== PROCESADOR DE GRAMÁTICA: PALÍNDROMOS BINARIOS ===")
    print("Gramática: S → 0S0 | 1S1 | 0 | 1")
    print("Acepta: Números capicúas con 0 y 1\n")
    
    if len(sys.argv) > 1:
        # Si se proporciona un archivo como argumento
        nombre_archivo = sys.argv[1]
        print(f"Procesando archivo: {nombre_archivo}")
        print("-" * 50)
        procesar_archivo(nombre_archivo)
    else:
        # Modo interactivo
        print("Modo interactivo:")
        print("1. Escriba un archivo .txt para procesar")
        print("2. Escriba una cadena para validar individualmente")
        print("3. Escriba 'salir' para terminar\n")
        
        while True:
            entrada = input("Ingrese archivo o cadena: ").strip()
            
            if entrada.lower() == 'salir':
                print("¡Hasta luego!")
                break
            elif entrada.endswith('.txt'):
                if os.path.exists(entrada):
                    print(f"\nProcesando archivo: {entrada}")
                    print("-" * 50)
                    procesar_archivo(entrada)
                    print("-" * 50)
                else:
                    print(f"Error: El archivo '{entrada}' no existe.")
            else:
                # Validar como cadena individual
                print(f"Validando: '{entrada}'")
                validar_cadena_individual(entrada)
            print()

# Ejemplos de uso y pruebas
def ejecutar_pruebas():
    """
    Ejecuta algunas pruebas de ejemplo.
    """
    print("=== PRUEBAS DE EJEMPLO ===")
    pruebas = [
        "0",      # ACEPTO (caso base)
        "1",      # ACEPTO (caso base)  
        "00",     # ACEPTO (0S0 donde S→0)
        "11",     # ACEPTO (1S1 donde S→1)
        "010",    # ACEPTO (0S0 donde S→1)
        "101",    # ACEPTO (1S1 donde S→0)
        "0110",   # ACEPTO (0S0 donde S→11)
        "1001",   # ACEPTO (1S1 donde S→00)
        "01010",  # ACEPTO
        "10101",  # ACEPTO
        "001100", # ACEPTO
        "110011", # ACEPTO
        "01",     # NO ACEPTA (no es palíndromo)
        "10",     # NO ACEPTA (no es palíndromo)
        "012",    # NO ACEPTA (contiene 2)
        "abc",    # NO ACEPTA (no binario)
        "0011",   # NO ACEPTA (no es palíndromo)
        "",       # NO ACEPTA (cadena vacía)
    ]
    
    for prueba in pruebas:
        resultado = "ACEPTO" if es_palindromo_binario(prueba) else "NO ACEPTA"
        print(f"'{prueba}' -> {resultado}")

if __name__ == "__main__":
    # Uncomment the next line to run tests
    # ejecutar_pruebas()
    main()