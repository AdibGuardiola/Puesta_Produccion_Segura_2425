# Cargar los datos del archivo de usuarios registrados
with open(r'C:\Users\Usuario\Desktop\PUK_Docker-Git\GeneradordeClaves\usuarios_registrados.txt', 'r') as file:
    usuarios_registrados = file.readlines()

# Cargar las posibles contraseñas desde un archivo
with open(r'C:\Users\Usuario\Desktop\PUK_Docker-Git\GeneradordeClaves\posibles_contraseñas.txt', 'r') as file:
    posibles_contraseñas = file.readlines()

# Función para intentar romper la contraseña de un usuario específico
def fuerza_bruta_para_usuario(usuario_objetivo):
    # Buscar al usuario en el archivo de usuarios registrados
    usuario_encontrado = False
    contraseña_objetivo = None
    
    for login in usuarios_registrados:
        # Asegurarse de que la línea tiene el formato correcto: 'Usuario: email, Contraseña: contraseña'
        if ', Contraseña: ' in login:
            # Separar el email y la contraseña
            registered_email, registered_password = login.strip().split(', Contraseña: ')
            # Limpiar los prefijos 'Usuario: ' y 'Contraseña: '
            registered_email = registered_email.replace("Usuario: ", "").strip().lower()
            registered_password = registered_password.strip()

            # Comparar el usuario en minúsculas para evitar errores
            if registered_email == usuario_objetivo.lower():
                usuario_encontrado = True
                contraseña_objetivo = registered_password
                break

    if usuario_encontrado:
        print(f"Intentando romper la contraseña del usuario: {usuario_objetivo}")
        encontrada = False  # Bandera para verificar si se encontró la contraseña

        for intento_contraseña in posibles_contraseñas:
            intento_contraseña = intento_contraseña.strip()  # Quitar espacios en blanco

            # Depuración: imprimir el intento de contraseña
            print(f"Intentando contraseña: {intento_contraseña}")

            # Comparar la contraseña objetivo con la contraseña del archivo
            if intento_contraseña == contraseña_objetivo:
                print(f"¡Contraseña encontrada para {usuario_objetivo}: {intento_contraseña}")
                encontrada = True
                break  # Termina el intento para este usuario

        if not encontrada:
            print(f"No se encontró la contraseña para el usuario {usuario_objetivo}")
    else:
        print(f"El usuario {usuario_objetivo} no fue encontrado.")

# Definir el usuario a probar (predefinido)
usuario_a_probar = "juan.perez@gmail.com"
fuerza_bruta_para_usuario(usuario_a_probar)
