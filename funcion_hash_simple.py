"""Utility script to generate hashes for given text using various algorithms."""

import hashlib # librería para generar hash

def mi_hash_simple(texto, algoritmo='sha1'):
    """Implementa una función simple ingresando  ``texto`` retorna el hash de ``algoritmo``."""
    hasher = hashlib.new(algoritmo, texto.encode('utf-8')) # crea un objeto hasher
    return hasher.hexdigest() # retorna el hash en formato hexadecimal

print(mi_hash_simple("hola "))