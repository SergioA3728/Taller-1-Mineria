#imports
import pandas as pd
import numpy as np
import random
#configs
n = 500
np.ramdom.seed(42)
#variales
Edad= np.ramdom.ramdint(16,30,n)
Genero= np.ramdon.choice (['M','F'],n)
Lugar_origen= np.ramdon.choice (['soledad','Sabana larga','Sabana Grande','Baranoa','Barranquilla'],n)
PM_bachiderato= np.round(np.ramdon.uniform(2.0,5.0,n),2)
ICFES= np.round(np.ramdon.uniform(200,500,n),2)
NT_Semestre1= np.round(np.ramdon.uniform(2.0,5.0,n),2)
Estrato= np.ramdon.choice ([1,2,3,4,5,6],n)
Beca= np.ramdon.choice (['Si','No'],n)
Icetex= np.ramdon.choice (['Si','No'],n)
Desercion= np.where((PM_bachiderato<3.0)|(NT_Semestre1<3.0),
                    np.ramdon.choice (['Si','No'],n,p=[0.7,0.3]), 
                    np.ramdon.choice (['Si','No'],n,p=[0.2,0.8]))
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