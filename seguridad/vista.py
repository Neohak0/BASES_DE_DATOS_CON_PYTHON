from seguridad.usuario import Usuario

class MenuSeguridad:

    def mostrar_menu(self):
        while(True):
            print("=" * 50)
            print("= GESTION DE USUARIOS =")
            print("1. Iniciar sesion")
            print("2. Registrarse")
            print("0. Salir")
            opcion = int(input("Cual es su opcion: "))
            if opcion == 1:
                self.iniciar_sesion()
            elif opcion == 2:
                self.registro()
            elif opcion == 0:
                print("Hasta luego")
                break
    
    def iniciar_sesion(self):
        print("= INICIO DE SESION =")
        correo = input("Ingrese su correo: ")
        clave = input("Ingrese su contraseña: ")

        # Validar usuario y contraseña
        usuario = Usuario(correo, clave)
        estado = usuario.iniciar_sesion()

        if estado:
            print("Usuario iniciado exitosamente")
            # TODO Entrar a la aplicación de tareas
        else:
            print("Credenciales inválidas. Intente de nuevo")

    def registro(self):
        print("= REGISTRO DE USUARIO =")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        clave = input("Ingrese su contraseña: ") 

        # Guardar en base de datos
        # usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, clave=clave)
        usuario = Usuario(correo, clave, nombre, apellido)
        guardado = usuario.registrar()

        if guardado:
            print("Usuario guardado correctamente")
        else:
            print("Ha ocurrido un error al guardar el usaurio")
    