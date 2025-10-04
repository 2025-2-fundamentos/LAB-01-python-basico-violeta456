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



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    data=open_csv("files/input/data.csv")

    registros_clave={}
    for row in data:
        elementos=row[4].strip().split(",")
        for clave_valor in elementos:
            clave,valor=clave_valor.split(":")
            if clave not in registros_clave:
                registros_clave[clave]=[float("inf"),0]
            
            registros_clave[clave]=[min(registros_clave[clave][0],int(valor)),max(registros_clave[clave][1],int(valor))]
    
    respuesta=[]
    for key,value in registros_clave.items():
        respuesta.append((key,value[0],value[1]))

    return sorted(respuesta)
pregunta_06()
