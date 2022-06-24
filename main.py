from calculadora.operaciones import sumar
from calculadora.operaciones import restar
from calculadora.operaciones import multiplicar
from calculadora.operaciones import dividir


def main():
    suma = sumar(10,12,14,16,18,20)
    print(suma)
    resta = restar(3,5,-5,9,-2)
    print(resta)
    prod = multiplicar(10,12,-2)
    print(prod)
    divi = dividir(8,4,4,0.125)
    print(divi)


if(__name__ == "__main__"):
    main()