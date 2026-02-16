"""Utility script to generate hashes for given text using various algorithms."""

import hashlib # librería para generar hash


## Implementación simple de hash, UTILIZANDO la librería hashlib.
def mi_hash_simple_hashlib(texto, algoritmo='sha1'):
    """Implementa una función simple ingresando  ``texto`` retorna el hash de ``algoritmo``."""
    hasher = hashlib.new(algoritmo, texto.encode('utf-8')) # crea un objeto hasher
    return hasher.hexdigest() 

#Implementación simple de hash, NO UTILIZANDO la librería hashlib.
def mi_hash_simple(texto, algoritmo='sha1'):
    """Implementa una función simple ingresando ``texto`` retorna el hash de ``algoritmo``."""
    # Implementación simple de hash (no criptográfico)
    hash_value = 0
    for char in texto:
        # Usa una operación simple: (hash * 31 + ord(char)) mod 2^32
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF
    
    # Convierte a hexadecimal (simula el formato de SHA1 con 40 caracteres)
    if algoritmo == 'sha1':
        # Expande el hash para que parezca SHA1 (40 caracteres hex)
        return format(hash_value, '08x') * 5
    else:
        return format(hash_value, '08x')

if __name__ == "__main__":
    print("[HASHLIB]", mi_hash_simple_hashlib("hola"))
    print("[SIMPLE]", mi_hash_simple("hola "))