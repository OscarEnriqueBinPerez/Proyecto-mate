import math

def fx(x):
    return math.sin(x) / x if x != 0 else 1  # Manejo del caso x = 0

def integral_simpson(a, b, n):
    if n % 2 == 1:
        n += 1  # Simpson requiere un número par de subintervalos
    delta_x = (b - a) / n
    suma = fx(a) + fx(b)
    for i in range(1, n, 2):
        suma += 4 * fx(a + i * delta_x)
    for i in range(2, n-1, 2):
        suma += 2 * fx(a + i * delta_x)
    return (delta_x / 3) * suma

def main():
    a = math.pi / 2
    b = 3 * math.pi / 2
    n = int(input("Ingresa el número de subintervalos (debe ser par) para la aproximación: "))
    aproximacion = integral_simpson(a, b, n)
    print("La aproximación de la integral es:", aproximacion)

if __name__ == '__main__':
    main()