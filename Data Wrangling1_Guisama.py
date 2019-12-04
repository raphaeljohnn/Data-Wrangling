import pandas as pd
Math= {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
Electronics= {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
GEAS= {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
ESAT= {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
Math1=pd.DataFrame(Math,columns=['Student','Math'])
Electronics1=pd.DataFrame(Electronics,columns=['Student','Electronics'])
GEAS1=pd.DataFrame(GEAS,columns=['Student','GEAS'])
ESAT1=pd.DataFrame(ESAT,columns=['Student','ESAT'])

wbb=pd.merge(Math1,Electronics1,how='inner', on='Student')
wbb2=pd.merge(wbb,GEAS1,how='inner', on='Student')
wbb3=pd.merge(wbb2,ESAT1,how='inner', on='Student')

longformat= wbb3.melt(id_vars=['Student'], var_name='Subject', value_name='Grades')
longformat2= longformat.sort_values('Student')