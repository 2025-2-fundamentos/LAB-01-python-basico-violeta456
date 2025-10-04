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

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data=open_csv("files/input/data.csv")
    registros_letra={}

    for row in data:
        letra=row[0].strip()
        if letra not in registros_letra:
            registros_letra[letra]=[]
        registros_letra[letra].append(int(row[1]))

    respuesta=[]
    for key,value in registros_letra.items():
        maximo=max(value)
        minimo=min(value)
        respuesta.append((key,maximo,minimo))
    
    return sorted(respuesta)

pregunta_05()

