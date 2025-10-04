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

   


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    data=open_csv("files/input/data.csv")
    registros_mes={}
    for row in data:
        mes=row[2].split("-")[1]
        if mes not in registros_mes:
            registros_mes[mes]=0
        registros_mes[mes]+=1

    tuplas_respuesta=[]
    for key,value in registros_mes.items():
        tuplas_respuesta.append((key,value))

    return sorted(tuplas_respuesta)

pregunta_04()
#print(pregunta_04())