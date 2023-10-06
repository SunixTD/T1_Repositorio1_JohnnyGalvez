class Calculadora:
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "No se puede dividir por cero."
        else:
            return a / b

if __name__ == "__main__":
    calc = Calculadora()
    
    try:
        num1 = int(input("Ingrese el primer valor entero: "))
        num2 = int(input("Ingrese el segundo valor entero: "))
        
        resultado_suma = calc.suma(num1, num2)
        resultado_resta = calc.resta(num1, num2)
        resultado_multiplicacion = calc.multiplicacion(num1, num2)
        resultado_division = calc.division(num1, num2)
        
        print(f"Suma: {resultado_suma}")
        print(f"Resta: {resultado_resta}")
        print(f"Multiplicación: {resultado_multiplicacion}")
        print(f"División: {resultado_division}")
    
    except ValueError:
        print("Error: Ingrese valores enteros válidos.")