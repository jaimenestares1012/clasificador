import numpy as np

import pandas as pd
from textblob.classifiers import NaiveBayesClassifier

with open('DataEntrenada.json', 'r') as fp: #### Se abre el archivo que contiene a la data entrenada
    cl=NaiveBayesClassifier(fp, format="json")  ### se le asigna la variable cl

datos=pd.read_csv('dataset.csv', encoding='latin-1', header=0 , sep=";") #####leemmos el df, que hemos obtenido del portal de datos abiertos
df=pd.DataFrame(datos)                                          ## se convierte el archivo leído a un dataframe(DF)
###df.dropna(how='all')  ###elimina filas que todas tengan N/A

df=df.fillna({'Column1':0}) ## rellenamos la ultima columna con valores 0
i=0
for f in range(df.shape[0]):###iteramos sobre los indices del dataframe
    try:
        estado = cl.classify(df.OCUPACIONES[f]) ### hacemos el análisis con la data entrenada
        if (estado =="1"):      ## si el resultado es igual a (1-->pertenece a lo requerido)
            i = i + 1           ## Se adjunta un contador, para saber cuantas tipos de trabajos hay
            df.Column1[f]=1         ### SE LE DA EL VALOR DE 0-->1, ESTO MAS ADELANTE NOS SERVIRÁ PARA HACER EL FILTRO

    except:
        Exception
print(i)

df=df[df["Column1"]>0]             #### CREAMOS UN DF CON EL MISMO NOMBRE, PERO CON LA CONDICION QUE SEA MAYOR QUE 0, OSEA 1

df.to_csv('data_clasificada.csv', index=False)  #### EXPORTAMOS EL DF, PARA UN ANALISIS EN RSTUDIO
