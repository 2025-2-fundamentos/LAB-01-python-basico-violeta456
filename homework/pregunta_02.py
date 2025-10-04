"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    registros_letra={}
    archivo = "files/input/data.csv"
    with open (archivo, "r",encoding="utf-8") as file:
        reader=csv.reader(file,delimiter="\t")
        for row in reader:
            letra=row[0].strip()
            if letra not in registros_letra:
                registros_letra[letra]=0
            registros_letra[letra]+=1
    
    tuplas_respuesta=[]
    for key,value in registros_letra.items():
        tuplas_respuesta.append((key,value))

    return sorted(tuplas_respuesta)

pregunta_02()
