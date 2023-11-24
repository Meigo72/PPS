def fibonacci(n):
    secuencia = [0, 1]

    for i in range(2, n):
        siguiente_num = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_num)

    return secuencia

def main():
    try:
        n = int(input("Cuantos términos quieres generar: "))

        if n <= 0:
            print("Tiene que ser un número entero positivo.")
        else:
            resultado = fibonacci(n)
            print(f"La secuencia de Fibonacci con {n} términos es: {resultado}")

    except ValueError:
        print("Ingresa un número entero válido.")

if __name__ == "__main__":
    main()
