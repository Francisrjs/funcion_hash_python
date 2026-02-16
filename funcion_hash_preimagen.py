"""Ataque de preimagen: intenta encontrar un texto que produzca un hash objetivo."""

import hashlib  # librería para generar hash
import random  # librería para generar números aleatorios
import string  # librería para generar cadenas aleatorias
import time  # librería para medir el tiempo


TARGET_HASH = "99800b85d3383e3a2fb45eb7d0066a4879a9dad0"  # SHA1("hola")


def buscar_preimagen(target_hash, algoritmo="sha1", long_cad=10, max_intentos=1_000_000):
    """Devuelve un diccionario con la cadena encontrada, intentos y tiempo que tomó."""

    intentos = 0
    inicio = time.time()

    while intentos < max_intentos:
        input_rand = "".join(
            random.choices(string.ascii_letters + string.digits, k=long_cad)
        )
        h = hashlib.new(algoritmo, input_rand.encode("utf-8")).hexdigest()
        intentos += 1
        registrar_progreso(intentos)

        if h == target_hash:
            tiempo = time.time() - inicio
            return {
                "valor": input_rand,
                "intentos": intentos,
                "tiempo": tiempo,
                "hash": h,
            }

    return {"valor": None, "intentos": intentos, "tiempo": time.time() - inicio, "hash": None}


def registrar_progreso(intentos, cada=100000):
    """Escribe en consola cada `cada` iteraciones para monitorear el ataque."""

    if intentos % cada == 0:
        print(f"[PREIMAGEN][{intentos}] Iteraciones completadas")


if __name__ == "__main__":
    print("[PREIMAGEN] Iniciando búsqueda de preimagen")
    resultado = buscar_preimagen(TARGET_HASH)
    registrar_progreso(resultado["intentos"])

    if resultado["valor"]:
        print("[PREIMAGEN] ✓ Preimagen encontrada")
        print(f"[PREIMAGEN] Texto: {resultado['valor']}")
        print(f"[PREIMAGEN] Hash objetivo: {TARGET_HASH}")
        print(f"[PREIMAGEN] Intentos: {resultado['intentos']}")
        print(f"[PREIMAGEN] Tiempo: {resultado['tiempo']:.4f}s")
    else:
        print("[PREIMAGEN] ✗ No se encontró preimagen en el límite de intentos")
