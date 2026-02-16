import hashlib
import random
import string
import time

def buscar_colision(algoritmo='sha1', long_cad=10, max_intentos=1000000):
    # Busca colisiones de hash generando cadenas aleatorias
    intentos = 0
    hashes_vistos = {}
    inicio = time.time()
    
    while intentos < max_intentos:
        # Genera una cadena aleatoria de caracteres
        input1 = ''.join(random.choices(string.ascii_letters + string.digits, k=long_cad))
        h = hashlib.new(algoritmo, input1.encode()).hexdigest()
        intentos += 1
        
        if h in hashes_vistos:
            input2 = hashes_vistos[h]
            tiempo = time.time() - inicio
            return input1, input2, h, intentos, tiempo
        hashes_vistos[h] = input1
    
    return None, None, None, intentos, time.time() - inicio

# Ejecuta la búsqueda de colisiones y verifica si encontró una real
resultado = buscar_colision()
if resultado[0] is not None:
    input1, input2, hash_comun, intentos, tiempo = resultado
    if input1 != input2:
        print(f" COLISIÓN ENCONTRADA!")
        print(f"  Input 1: {input1}")
        print(f"  Input 2: {input2}")
        print(f"  Hash común: {hash_comun}")
        print(f"  Intentos: {intentos}, Tiempo: {tiempo:.4f}s")
    else:
        print(" No es colisión (misma entrada)")
else:
    print(" No se encontró colisión en los intentos")