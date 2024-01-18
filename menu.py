from buyer import Buyer
from admin import Admin

class Menu:
    def __init__(self):
        self.buyer = Buyer()
        self.admin = Admin()

    def run(self):
        while True:
            print("\nBienvenido a la Tienda Virtual:")
            print("1. Panel Administrador")
            print("2. Panel Comprador")
            print("3. Salir")
            opcion_principal = input("Seleccione una opción: ")

            if opcion_principal == "1":
                self.admin.panel_administrador()
            elif opcion_principal == "2":
                self.buyer.panel_comprador()
            elif opcion_principal == "3":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
