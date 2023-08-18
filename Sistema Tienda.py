class Tienda:
    def __init__(self):
        self.usuarios = {
            "usuario1": {"contraseña": "contraseña123", "saldo": 100.000},
            "usuario2": {"contraseña": "abc123", "saldo": 150.000}
        }
        
        self.productos = {
            "producto1": 59.999,
            "producto2": 75.000,
            "producto3": 119.999
        }
        
        self.moneda = "monedas"
    
    def iniciar_sesion(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if usuario in self.usuarios and self.usuarios[usuario]["contraseña"] == contraseña:
            return usuario
        else:
            print("Credenciales inválidas.")
            return None
    
    def mostrar_productos(self):
        print("Productos disponibles:")
        for producto, precio in self.productos.items():
            print(f"{producto}: {precio} {self.moneda}")
    
    def comprar_producto(self, usuario):
        self.mostrar_productos()
        producto = input("Ingrese el nombre del producto que desea comprar: ")
        
        if producto in self.productos:
            precio = self.productos[producto]
            if self.usuarios[usuario]["saldo"] >= precio:
                self.usuarios[usuario]["saldo"] -= precio
                print(f"¡Compra exitosa! Se redujeron {precio} {self.moneda} de su saldo.")
            else:
                print("Saldo insuficiente para realizar la compra.")
        else:
            print("Producto no encontrado.")
    
    def mostrar_saldo(self, usuario):
        saldo_actual = self.usuarios[usuario]["saldo"]
        print(f"Su saldo actual es: {saldo_actual} {self.moneda}")


def main():
    tienda = Tienda()
    print("Bienvenido a la Tienda Virtual!")
    
    while True:
        print("\nPresione '1' para iniciar sesión")
        print("Presione '2' para salir")
        
        eleccion = input("Ingrese su elección: ")
        
        if eleccion == "1":
            usuario_actual = tienda.iniciar_sesion()
            if usuario_actual:
                while True:
                    print("\nPresione '1' para ver productos disponibles")
                    print("Presione '2' para comprar un producto")
                    print("Presione '3' para ver su saldo")
                    print("Presione '4' para cerrar sesión")
                    
                    opcion = input("Ingrese su opción: ")
                    
                    if opcion == "1":
                        tienda.mostrar_productos()
                    elif opcion == "2":
                        tienda.comprar_producto(usuario_actual)
                    elif opcion == "3":
                        tienda.mostrar_saldo(usuario_actual)
                    elif opcion == "4":
                        print("Cerrando sesión. ¡Hasta pronto!")
                        break
                    else:
                        print("Opción inválida. Por favor, intente nuevamente.")
        elif eleccion == "2":
            print("Saliendo. ¡Hasta pronto!")
            break
        else:
            print("Elección inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()