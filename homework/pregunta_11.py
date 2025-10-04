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

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    data=open_csv("files/input/data.csv")
    registro_letra={}
    for row in data:
        elementos=row[3].split(",")
        for valor in elementos:
            if valor not in registro_letra:
                registro_letra[valor]=0
            
            registro_letra[valor]+=int(row[1])
    
    return registro_letra

pregunta_11()


