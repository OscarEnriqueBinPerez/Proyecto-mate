import math

def fx(x):
    #x/sqrt(2x+1)
    return x / math.sqrt(2 * x + 1)
def integral_rectangulos(a, b, n):
    delta_x = (b-a)/n
    suma = 0;
    for i in range(n):
        af = a + delta_x
        x = (a+af)/2
        suma += fx(x)
        a = af
    return suma * delta_x

def main():
    a = float(input("ingresa el limite inferior de la integral: "))
    b = float(input("ingresa el limite superior de la integral: "))
    n = int(input("ingresa el numero de rectangulos para la aproximacion: "))
    aproximacion = integral_rectangulos(a,b,n)

    print("La aproximacion de la integral es: ",aproximacion)

if __name__ == '__main__':
    main() 
