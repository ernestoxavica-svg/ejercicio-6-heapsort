"""
Ordenamiento Heapsort
Menú que pide la cantidad de números y los números, los ordena con
Heapsort y repite hasta que el usuario decida salir.
"""


def heap_sort(lista):
    """Ordena una lista de enteros con Heapsort (montículo máximo)."""
    arr = lista.copy()
    n = len(arr)

    # 1) Construir el montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # 2) Extraer el mayor elemento uno por uno
    for fin in range(n - 1, 0, -1):
        arr[0], arr[fin] = arr[fin], arr[0]   # el máximo va al final
        _heapify(arr, fin, 0)                 # reparar el montículo
    return arr


def _heapify(arr, n, i):
    """Hunde el elemento en la posición i hasta cumplir la propiedad del heap."""
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        _heapify(arr, n, mayor)


def pedir_entero(mensaje, minimo=None):
    """Pide un entero por teclado y repite hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida, escribe un número entero.")


def pedir_numeros():
    """Pide la cantidad de números y luego cada número."""
    cantidad = pedir_entero("¿Cuántos números deseas ordenar? ", minimo=1)
    numeros = []
    for i in range(cantidad):
        numeros.append(pedir_entero(f"  Número {i + 1}: "))
    return numeros


def menu():
    print("\n===== ORDENAMIENTO HEAPSORT =====")
    print("1. Ordenar números")
    print("2. Salir")


def main():
    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            numeros = pedir_numeros()
            print("\nLista original :", numeros)
            print("Lista ordenada :", heap_sort(numeros))
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()