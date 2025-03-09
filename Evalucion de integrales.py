import math
from scipy.integrate import quad

def fx(x):
    return x / math.sqrt(2 * x + 1)

def main():
    a = float(input("Ingresa el límite inferior de la integral: "))
    b = float(input("Ingresa el límite superior de la integral: "))

    resultado, error = quad(fx, a, b)  # Calcula la integral y el error estimado
    print("La aproximación de la integral es:", resultado)
    print("Error estimado:", error)

if __name__ == '__main__':
    main()