"""Utility script to generate hashes for given text using various algorithms."""

import hashlib

def mi_hash_simple(texto, algoritmo='sha1'):
    """Implementa una función simple ingresando  ``texto`` retorna el hash de ``algoritmo``."""
    hasher = hashlib.new(algoritmo, texto.encode('utf-8'))
    return hasher.hexdigest()

print(mi_hash_simple("hola"))