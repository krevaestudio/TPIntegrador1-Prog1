import time

def fibonacci_recursivo(num):
    if num <= 1:
        return num
    return fibonacci_recursivo(num-1) + fibonacci_recursivo(num-2)

def fibonacci_iterativo(num):
    if num <= 1:
        return num
    a, b = 0, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return b

def medir_tiempo(funcion, num):
    """Mide el tiempo de ejecución de una función dada."""
    inicio = time.time()
    resultado = funcion(num)
    fin = time.time()
    return resultado, fin - inicio

if __name__ == "__main__":
    
    num_peq = 40

    print(f"Calculando Fibonacci para n = {num_peq}...\n")

    resultado1, tiempo1 = medir_tiempo(fibonacci_recursivo,num_peq)
    print(f"Fibonacci Recursivo: Resultado={resultado1}, Tiempo={tiempo1:.6f} segundos")

    resultado2, tiempo2 = medir_tiempo(fibonacci_iterativo,num_peq)
    print(f"Fibonacci Iterativo: Resultado={resultado2}, Tiempo={tiempo2:.6f} segundos")

    n_grande = 1000000
    print(f"\nCalculando Fibonacci para n = {n_grande} con el método iterativo...")
    _,tiempo_grande = medir_tiempo(fibonacci_iterativo, n_grande)
    print(f"Fibonacci Iterativo (n={n_grande}): Tiempo={tiempo_grande:.6f} segundos")
