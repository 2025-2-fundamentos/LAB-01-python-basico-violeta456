"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Suma
    suma=0

    # Abrir el archivo
    archivo = "files/input/data.csv"
    with open (archivo,"r",encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            suma+=int(row[1])

    return suma
    
pregunta_01()