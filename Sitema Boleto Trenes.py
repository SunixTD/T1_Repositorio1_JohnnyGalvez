class MaquinaBoletos:
    def __init__(self):
        self.destinos = {
            "Pasto": 50.000,  
            "Cali": 80.000,  
            "Bogota": 120.000  
        }

    def mostrar_destinos(self):
        print("Destinos:")
        for dest, precio in self.destinos.items():
            print(f"{dest}: ${precio}")

    def emitir_boleto(self, destino, tarjeta_credito, pin):
        if destino not in self.destinos:
            print("Destino inválido.")
            return
        
        precio = self.destinos[destino]
        
        if self.validar_tarjeta_credito(tarjeta_credito, pin, precio):
            print("¡Boleto emitido exitosamente!")
        else:
            print("Fallo en la validación de la tarjeta de crédito.")

    def validar_tarjeta_credito(self, tarjeta_credito, pin, monto):
       
        return True  


def main():
    maquina_boletos = MaquinaBoletos()
    print("Bienvenido a trenes Bolivariano!")
    
    while True:
        print("\nPresione '1' para ver destinos")
        print("Presione '2' para emitir un boleto")
        print("Presione '3' para salir")
        
        eleccion = input("Ingrese su elección: ")
        
        if eleccion == "1":
            maquina_boletos.mostrar_destinos()
        elif eleccion == "2":
            destino = input("Ingrese el destino: ").upper()
            tarjeta_credito = input("Ingrese el número de tarjeta de crédito: ")
            pin = input("Ingrese su PIN: ")
            maquina_boletos.emitir_boleto(destino, tarjeta_credito, pin)
        elif eleccion == "3":
            print("Saliendo. ¡Que tenga un buen viaje!")
            break
        else:
            print("Elección inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()