import cita
import os

if __name__ == '__main__':
    try:
        bandera = True
        while (bandera):
            print("1. Gestionar citas")
            print("2. Salir")
            opc = int(input("Ingrese la opcion: "))
            if (opc == 1):
                os.system('clear')
                cita.menu()
            if (opc == 2):
                os.system("clear")
                print("Hasta luego")
                bandera = False
            if (opc < 1 or opc > 2):
                print('Opcion no valida')

    except Exception as e:
        print('Ingresó un dato incorrecto')
