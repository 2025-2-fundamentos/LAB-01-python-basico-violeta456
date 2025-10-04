"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def open_csv(file_path):
    import csv
    with open(file_path,"r",encoding="utf-8") as file:
        reader=csv.reader(file,delimiter="\t")
        reader=list(reader)
    return reader


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    data = open_csv("files/input/data.csv")

    registros_clave = {}
    for row in data:
        elementos = row[4].split(",")
        for clave_valor in elementos:
            clave,_ = clave_valor.split(":")
            if clave not in registros_clave:
                registros_clave[clave] = 0
            registros_clave[clave] += 1
    


    return registros_clave

pregunta_09()



