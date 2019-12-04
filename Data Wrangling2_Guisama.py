import pandas as pd
DF= {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension':['Length','Width','Height','Length','Width','Height'],
         'Value':[6,4,2,5,3,4]}
Messy=pd.DataFrame(DF,columns=['Box','Dimension','Value'])
Tidy=Messy.pivot(index='Box',columns='Dimension',values='Value').reset_index()
data= Tidy[['Height','Length','Width']].transpose().prod().tolist()
volume1= {'Box':['Box1','Box2'],
         'Volume':data}
volume=pd.DataFrame(volume1,columns=['Box','Volume'])
TidyVolume=pd.merge(Tidy,volume,how='inner', on='Box')