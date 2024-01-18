import json
from datetime import datetime
import os

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

class ProductManager:
    @staticmethod
    def agregar_producto():
        productos = FileManager.cargar_datos("productos.txt")
        producto = {
            'id': input("Ingrese el ID del producto: "),
            'nombre': input("Ingrese el nombre del producto: "),
            'precio': float(input("Ingrese el precio del producto: "))
        }
        productos.append(producto)
        FileManager.guardar_datos("productos.txt", productos)
        print("Producto agregado correctamente.")
    
    @staticmethod
    def editar_producto():
        productos = FileManager.cargar_datos("productos.txt")
        id_producto = input("Ingrese el ID del producto que desea editar: ")
        
        producto_existente = next((p for p in productos if p['id'] == id_producto), None)
        
        if producto_existente:
            print(f'Producto actual: {producto_existente}')
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (deje en blanco para mantener el actual): ")
            nuevo_precio = input("Ingrese el nuevo precio del producto (deje en blanco para mantener el actual): ")

            if nuevo_nombre:
                producto_existente['nombre'] = nuevo_nombre
            if nuevo_precio:
                producto_existente['precio'] = float(nuevo_precio)
            
            FileManager.guardar_datos("productos.txt", productos)
            print("Producto editado correctamente.")
        else:
            print("Producto no encontrado.")
            
    @staticmethod
    def eliminar_producto():
        productos = FileManager.cargar_datos("productos.txt")
        id_producto = input("Ingrese el ID del producto que desea eliminar: ")
        
        producto_existente = next((p for p in productos if p['id'] == id_producto), None)
        
        if producto_existente:
            print(f'Producto a eliminar: {producto_existente}')
            confirmacion = input("¿Esta seguro que desea eliminar este producto? (si/no): ").lower()
            
            if confirmacion == "si":
                productos.remove(producto_existente)
                FileManager.guardar_datos("productos.txt", productos)
                print("Producto eliminado correctamente.")
            else:
                print("Operacion cancelada.")
        else:
            print("Producto no encontrado.")
    
    @staticmethod
    def ver_productos():
        productos = FileManager.cargar_datos("productos.txt")
        
        if productos:
            print("\nLista de Productos:")
            for producto in productos:
                print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}")
        else:
            print("No hay productos disponibles.")

class UserManager:
    @staticmethod
    def ver_pedidos():
        pedidos = FileManager.cargar_datos("pedidos.txt")
        
        if pedidos:
            print("\nLista de Pedidos:")
            for pedido in pedidos:
                print(f"Usuario: {pedido.get('usuario', 'N/A')}, "
                      f"Producto: {pedido.get('nombre_producto', 'N/A')}, "
                      f"Cantidad: {pedido.get('cantidad', 'N/A')}, "
                      f"Total: ${pedido.get('total', 'N/A')}, "
                      f"Fecha: {pedido.get('fecha', 'N/A')}")
        else:
            print("No hay pedidos registrados.")
    
    @staticmethod
    def ver_usuarios():
        usuarios = FileManager.cargar_datos("usuarios.txt")
        
        if usuarios:
            print("\nLista de Usuarios:")
            for usuario in usuarios:
                print(f"Usuario: {usuario.get('usuario', 'N/A')}, "
                      f"Contraseña: {usuario.get('password', 'N/A')}")
        else:
            print("No hay nadie registrado.")

class Admin:
    def __init__(self):
        self.file_manager = FileManager()
        self.product_manager = ProductManager()
        self.users_manager = UserManager()

    def panel_administrador(self):
        usuario_admin = "admin"
        password_admin = "adminpass"

        admin_user = input("Ingrese el usuario: ")
        admin_pass = input("Ingrese la contraseña: ")

        if admin_user == usuario_admin and admin_pass == password_admin:
            while True:
                print("\nPanel Administrador:")
                print("1. Añadir producto")
                print("2. Editar producto")
                print("3. Eliminar producto")
                print("4. Ver productos")
                print("5. Ver pedidos")
                print("6. Ver usuarios")
                print("7. Salir")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self.product_manager.agregar_producto()
                elif opcion == "2":
                    self.product_manager.editar_producto()
                elif opcion == "3":
                    self.product_manager.eliminar_producto()
                elif opcion == "4":
                    self.product_manager.ver_productos()
                elif opcion == "5":
                    self.users_manager.ver_pedidos()
                elif opcion == "6":
                    self.users_manager.ver_usuarios()
                elif opcion == "7":
                    break
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
        else:
            print("Credenciales incorrectas. Saliendo.")
