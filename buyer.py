import json
import os
from datetime import datetime

class FileManager:
    @staticmethod
    def cargar_datos(archivo):
        if os.path.exists(archivo):
            with open(archivo, 'r') as file:
                return json.load(file)
        else:
            return []

    @staticmethod
    def guardar_datos(archivo, datos):
        with open(archivo, 'w') as file:
            json.dump(datos, file, indent=2)

class Login:
    @staticmethod
    def login():
        datos = FileManager.cargar_datos("usuarios.txt")

        usuario = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")

        for user in datos:
            if user['usuario'] == usuario and user['password'] == password:
                print('Inicio de sesión exitoso')
                return usuario

        print("\nCredenciales incorrectas.")
        opcion = input("(y) para intentarlo de nuevo y (n) para registro: ").lower()

        if opcion == "y":
            return Login.login()
        else:
            return Login.registrar_usuario()

    @staticmethod
    def registrar_usuario():
        usuarios = FileManager.cargar_datos("usuarios.txt")

        print("\nAún no tienes una cuenta. REGÍSTRATE")

        nuevo_usuario = {
            'usuario': input("Ingrese el nombre de usuario: "),
            'password': input("Ingrese la contraseña: ")
        }

        usuarios.append(nuevo_usuario)
        FileManager.guardar_datos("usuarios.txt", usuarios)
        print("Usuario registrado correctamente.")
        return nuevo_usuario["usuario"]

    @staticmethod
    def change_pass(usuario_actual):
        if usuario_actual:
            usuarios = FileManager.cargar_datos("usuarios.txt")
            usuario_existente = next((u for u in usuarios if u['usuario'] == usuario_actual), None)

            if usuario_existente:
                contraseña_actual = input("Ingrese la contraseña actual: ")

                if contraseña_actual == usuario_existente['password']:
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    usuario_existente['password'] = nueva_contraseña
                    FileManager.guardar_datos("usuarios.txt", usuarios)
                    print("Contraseña cambiada exitosamente.")
                else:
                    print("Contraseña actual incorrecta. Cancelado")
            else:
                print("Usuario no encontrado")
        else:
            print("Necesita iniciar sesión o registrarse primero.")

class Buyer(Login):
    def __init__(self):
        self.file_manager = FileManager()
        self.usuario_actual = None

    def panel_comprador(self):
        while True:
            print("\nPanel Comprador:")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.usuario_actual = self.login()
                self.comprando()
            elif opcion == "2":
                self.usuario_actual = self.registrar_usuario()
                self.comprando()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def comprar(self):
        productos = self.file_manager.cargar_datos("productos.txt")
        pedido_actual = []

        while True:
            print("\nProductos disponibles:")
            for producto in productos:
                print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']}")

            producto_id = input("Seleccione un producto (ID) o '0' para finalizar: ")

            if producto_id == "0":
                break

            cantidad = int(input("Ingrese la cantidad: "))
            producto_seleccionado = next((p for p in productos if p['id'] == producto_id), None)

            if producto_seleccionado:
                total = cantidad * producto_seleccionado['precio']
                pedido_actual.append({
                    'usuario': self.usuario_actual,
                    'nombre_producto': producto_seleccionado['nombre'],
                    'precio': producto_seleccionado['precio'],
                    'cantidad': cantidad,
                    'total': total,
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"Producto '{producto_seleccionado['nombre']}' agregado al carrito.")

        pedidos = self.file_manager.cargar_datos("pedidos.txt")
        pedidos.extend(pedido_actual)
        self.file_manager.guardar_datos("pedidos.txt", pedidos)

        print("Pedido realizado correctamente.")

    def comprando(self):
        while True:
            print(f"\nBIENVENIDO {self.usuario_actual}")
            print("1. Comprar")
            print("2. Cambiar contraseña")
            print("3. Salir")

            accion_comprador = input("Seleccione una opción: ")

            if accion_comprador == "1":
                self.comprar()
            elif accion_comprador == "2":
                self.change_pass(self.usuario_actual)
            elif accion_comprador == "3":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
