def ingresar_matriz():
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            cols = int(input("Ingrese el número de columnas: "))
            break
        except ValueError:
            print("Error: Ingrese números enteros.")

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            while True:
                try:
                    valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Debe ingresar un número.")
        matriz.append(fila)
    return matriz

def mostrar_matriz(A):
    for fila in A:
        print("[", " ".join(f"{val:g}" for val in fila), "]")
