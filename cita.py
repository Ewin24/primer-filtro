import datetime
import os
import core
import json


def menu():
    bandera = True
    while (bandera):
        os.system('clear')
        print('----------------------------------')
        print('    MENU DE CREACION DE CITAS     ')
        print('----------------------------------')
        print('1.Agregar cita')
        print('2.Modificar cita')
        print('3.Cancelar cita')
        print('4.Buscar cita')
        print('5.Regresar')
        opc = int(input('Ingrese la opcion que desea realizar: '))
        if (opc == 1):
            cita = {
                'paciente': input("Ingrese el nombre del paciente: "),
                'dia': input("Ingrese el dia en que se le asigno la cita (dd): "),
                'mes': input("Ingrese el mes en que se le asigno la cita (mm): "),
                'anio': input("Ingrese el año en que se le asigno la cita (AAAA): "),
                'motivo': input("Ingrese el motivo de la cita: ")
            }
            if (core.valFecha(cita['dia'], cita['mes'], cita['anio']) == ValueError):
                    print("su Fecha no es valida")
                    input()
            else:
                core.create('citas.json', cita)

        if (opc == 2):
            print('----------------------------------')
            print('         EDICION DE CITAS         ')
            print('----------------------------------')
            print("1. Buscar por nombre")
            print("2. Buscar por fecha")
            print("3. Salir")
            opc2 = int(input("Seleccione una opcion: "))
            if (opc2 == 1):
                nombre = input("Ingrese el paciente de la cita a editar: ")
                core.edit('citas.json', nombre, '', '', '')
            if (opc2 == 2):
                dia = input("Ingrese el dia de la cita: ")
                mes = input("Ingrese el mes de la cita: ")
                anio = input("Ingrese el año de la cita: ")
                if (core.valFecha(dia, mes, anio) == ValueError):
                    print("su Fecha no es valida")
                    input()
                else:
                    core.edit('citas.json', '', dia, mes, anio)
            if (opc2 == 3):
                pass
            else:
                print("Opcion no valida")

        if (opc == 3):
            print('----------------------------------')
            print('       CANCELACION DE CITAS       ')
            print('----------------------------------')
            print("1. Buscar por nombre")
            print("2. Buscar por fecha")
            print("3. Salir")
            opc3 = int(input("Seleccione una opcion: "))
            if (opc3 == 1):
                nombre = input("Ingrese el paciente de la cita a eliminar: ")
                core.delete('citas.json', nombre, '', '', '')
            if (opc3 == 2):
                dia = input("Ingrese el dia de la cita: ")
                mes = input("Ingrese el mes de la cita: ")
                anio = input("Ingrese el año de la cita: ")
                if (core.valFecha(dia, mes, anio) == ValueError):
                    print("su Fecha no es valida")
                    input()
                else:
                    core.delete('citas.json', '', dia, mes, anio)
            if (opc3 == 3):
                pass
            else:
                print("Opcion no valida")

        if (opc == 4):
            print('----------------------------------')
            print('         BUSQUEDA DE CITAS        ')
            print('----------------------------------')
            print("1. Buscar por nombre")
            print("2. Buscar por fecha")
            print("3. Salir")
            opc4 = int(input("Seleccione una opcion: "))
            if (opc4 == 1):
                nombre = input("Ingrese el paciente de la cita a buscar: ")
                core.listId('citas.json', nombre, '', '', '')
            if (opc4 == 2):
                dia = input("Ingrese el dia de la cita: ")
                mes = input("Ingrese el mes de la cita: ")
                anio = input("Ingrese el año de la cita: ")
                if (core.valFecha(dia, mes, anio) == ValueError):
                    print("su Fecha no es valida")
                    input()
                else:
                    core.listId('citas.json', '', dia, mes, anio)
            if (opc4 == 3):
                pass
            else:
                print("Opcion no valida")

        if (opc == 5):
            os.system('clear')
            bandera = False
