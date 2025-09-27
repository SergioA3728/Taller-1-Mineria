#imports
import pandas as pd
import numpy as np
import random
#configs
n = 500
np.random.seed(42)
#variales
Edad= np.random.randint(16,30,n)
Genero= np.random.choice (['M','F'],n)
Lugar_origen= np.random.choice (['soledad','Sabana larga','Sabana Grande','Baranoa','Barranquilla'],n)
PM_bachiderato= np.round(np.random.uniform(2.0,5.0,n),2)
ICFES= np.round(np.random.uniform(200,500,n),2)
NT_Semestre1= np.round(np.random.uniform(2.0,5.0,n),2)
Estrato= np.random.choice ([1,2,3,4,5,6],n)
Beca= np.random.choice (['Si','No'],n)
Icetex= np.random.choice (['Si','No'],n)
Desercion= np.where((PM_bachiderato<3.0)|(NT_Semestre1<3.0),
                    np.random.choice (['Si','No'],n,p=[0.7,0.3]), 
                    np.random.choice (['Si','No'],n,p=[0.2,0.8]))
#Muestra de datos
df = pd.DataFrame({
    'Edad': Edad,
    'Genero': Genero,
    'Lugar Origen': Lugar_origen,
    'Promedio del Bachiderato': PM_bachiderato,
    'ICFES': ICFES,
    'Notas Semestre #1': NT_Semestre1,
    'Estrato': Estrato,
    'Beca': Beca,
    'Credito Academico': Icetex,
    'Desercion': Desercion
})
#Datos Faltantes y Outliers
for col in ['Promedio del Bachiderato','Notas Semestre #1','Estrato']:
    df.loc[df.sample(frac=0.05).index,col]=np.nan
df.loc[random.sample(range(n), 5), 'Promedio del Bachiderato'] = 10 
df.loc[random.sample(range(n), 5), 'Edad'] = 45
#CSV
df.to_csv("Dataset_desercion_estudiantil.csv", index=False)

print("Archivo'Dataset_desercion_estudiantil.csv' generado con",len(df),"registros.")