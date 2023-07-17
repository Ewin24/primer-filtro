import datetime
import calendar


def valFecha(dia, mes, anio):
    try:
        return datetime.date(anio, mes, dia)
    except ValueError as e:
        return ValueError


print(valFecha(33, 12, 2023))