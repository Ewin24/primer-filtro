import json
import datetime
import cita


def create(filename, data):
    if (loadFile(filename) != False):
        # validar que no exista el id
        fileExist = loadFile(filename)
        for i, item in enumerate(fileExist['cita']):
            if item['paciente'] == data['paciente']:
                print("Ya existe un paciente con ese nombre en el sistema")
                input()
                cita.menu()
        else:
            fileExist = loadFile(filename)
            fileExist['cita'].append(data)
            file = open('data/'+filename, 'w')
            jsonObj = json.dumps(fileExist, indent=4)
            file.write(jsonObj)
            file.close()

    else:
        file = open('data/'+filename, 'w')
        jsonObj = json.dumps({'cita': [data]}, indent=4)
        file.write(jsonObj)
        file.close()

# importante usar el name como id


def edit(filename, nombre, dia, mes, anio):
    if (loadFile(filename) != False):
        fileExist = loadFile(filename)
        for i, item in enumerate(fileExist['cita']):
            if item['paciente'] == nombre or (item['dia'] == dia and item['mes'] == mes and item['anio'] == anio):
                fileExist['cita'].pop(i)  # borrar elemento
                print("---- Ingrese los nuevos datos ----")
                cita = {
                    'paciente': input("Ingrese el nuevo nombre del paciente: "),
                    'dia': input("Ingrese el nuevo dia en que se le asigno la cita (dd): "),
                    'mes': input("Ingrese el nuevo mes en que se le asigno la cita (mm): "),
                    'anio': input("Ingrese el nuevo año en que se le asigno la cita (AAAA): "),
                    'motivo': input("Ingrese el nuevo motivo de la cita: ")
                }
                fileExist['cita'].append(cita)  # agregar el elemento editado

                file = open('data/'+filename, 'w')
                jsonObj = json.dumps(fileExist, indent=4)
                file.write(jsonObj)
                file.close()
            else:
                print("El paciente no tiene citas para editar")
                input()
    else:
        print("No es posible editar datos si no existen registros")


def delete(filename, nombre, dia, mes, anio):
    if (loadFile(filename) != False):
        fileExist = loadFile(filename)
        for i, item in enumerate(fileExist['cita']):
            if item['paciente'] == nombre or (item['dia'] == dia and item['mes'] == mes and item['anio'] == anio):
                fileExist['cita'].pop(i)  # borrar elemento

                file = open('data/'+filename, 'w')
                jsonObj = json.dumps(fileExist, indent=4)
                file.write(jsonObj)
                file.close()
            else:
                print("No se encontro ninguna fecha del paciente")
    else:
        print("No es posible eliminar datos si no existen registros")


def listId(filename, nombre, dia, mes, anio):
    if (loadFile(filename) != False):
        fileExist = loadFile(filename)
        for i, item in enumerate(fileExist['cita']):
            if item['paciente'] == nombre or (item['dia'] == dia and item['mes'] == mes and item['anio'] == anio):
                print(
                    f" Nombre: {item['paciente']}\n Fecha de cita: {item['dia']}-{item['mes']}-{item['anio']} \n Motivo de cita: {item['motivo']}")
                input()
    else:
        print("No es posible buscar datos si no existen registros")


def loadFile(filename):
    try:
        with open('data/' + filename, 'r') as file:
            data = json.load(file)
            file.close()
            return data
    except FileNotFoundError as e:
        return False


def valFecha(dia, mes, anio):
    try:
        return datetime.date(int(anio), int(mes), int(dia))
    except ValueError as e:
        return ValueError
