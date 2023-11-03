# Clase Cliente
class Cliente:
    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.carrito_compras = []

    def agregar_producto_al_carrito(self, producto):
        self.carrito_compras.append(producto)
        print(f"{producto} agregado al carrito de compras de {self.nombre}.")

    def ver_carrito(self):
        if self.carrito_compras:
            print(f"Carrito de compras de {self.nombre}:")
            for producto in self.carrito_compras:
                print(producto)
        else:
            print(f"El carrito de compras de {self.nombre} está vacío.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Diccionario para almacenar usuarios y contraseñas
base_de_datos = {}

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    
    if nombre_usuario in base_de_datos and base_de_datos[nombre_usuario] == contrasena:
        print("Inicio de sesión exitoso.")
        return nombre_usuario
    else:
        print("Inicio de sesión fallido. Verifique su nombre de usuario y contraseña.")
        return None

# Menú principal
while True:
    print("\n--- Registro y Autenticación de Usuarios ---")
    print("1. Registrar nuevo usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Iniciar sesión")
    print("4. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == '1':
        registrar_usuario()
    
    elif opcion == '2':
        mostrar_usuarios()
    
    elif opcion == '3':
        nombre_usuario = iniciar_sesion()
        if nombre_usuario:
            cliente_actual = Cliente(nombre_usuario, "", "", "")
            print(f"Bienvenido, {cliente_actual}!")
            while True:
                print("\n--- Página de Compras ---")
                print("1. Agregar producto al carrito")
                print("2. Ver carrito de compras")
                print("3. Salir")
                
                opcion_compras = input("Elija una opción: ")
                
                if opcion_compras == '1':
                    producto = input("Ingrese el nombre del producto a agregar al carrito: ")
                    cliente_actual.agregar_producto_al_carrito(producto)
                
                elif opcion_compras == '2':
                    cliente_actual.ver_carrito()
                
                elif opcion_compras == '3':
                    print(f"¡Hasta luego, {cliente_actual}!")
                    break
                
                else:
                    print("Opción no válida. Por favor, elija una opción válida.")
    
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
