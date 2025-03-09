import math

def fx(x):
    return math.sin(x) / x if x != 0 else 1  # Manejo del caso x = 0

def integral_rectangulos(a, b, n):
    delta_x = (b - a) / n
    suma = 0
    for i in range(n):
        af = a + delta_x
        x = (a + af) / 2  # Punto medio
        suma += fx(x)
        a = af
    return suma * delta_x

def main():
    a = math.pi / 2
    b = 3 * math.pi / 2
    n = int(input("Ingresa el número de rectángulos para la aproximación: "))
    aproximacion = integral_rectangulos(a, b, n)
    print("La aproximación de la integral es:", aproximacion)

if __name__ == '__main__':
    main()
