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

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    data=open_csv("files/input/data.csv")
    registro_letra={}
    for row in data:
        letra=row[0].strip()
        if letra not in registro_letra:
            registro_letra[letra]=0
        
        elementos=row[4].split(",")
        suma=0

        for clave_valor in elementos:
            _,valor=clave_valor.split(":")
            suma+=int(valor)
        registro_letra[letra]+=suma
    return registro_letra

print(pregunta_12())
