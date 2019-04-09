import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dados = pd.read_csv('jvar-2018-09-18.csv')

dados.loc[:,'OBJECT']= dados.loc[:,'OBJECT'].str[:-6] 

filter_mapping = {
	'gSDSS':480.3,
	'J0378':378.5,
	'J0515':515.0,
	'rSDSS':625.4,
	'J0660':660.0,
	'iSDSS':766.8,
	'J0861':861.0,
	'J0395':395.0
}
dados.loc[:,'FILTER'] = dados.loc[:,'FILTER'].replace(filter_mapping)
data = dados.loc[:,'Name'].str[4:-4]
dados.loc[:,'OBJECT'] = dados.loc[:,'OBJECT'].str.replace('e', '')
data = pd.to_datetime(data, format = "%Y%m%dT%H%M%S")
dados.index = data
alt = dados.sort_values(by=['OBJECT'])
#alt = alt[alt.ExpTime != 10]
d = alt.pivot(columns='OBJECT',values='FILTER')
d.iloc[:,:].plot(style = 'o', legend = True)
#plt.show()
#f= alt.pivot(columns='FILTER',values='ExpTime') >> verificar o filtro r
#f[625.4]= f[625.4].replace(10,np.nan)

#for col in d.columns: >>>> salvar as imagens
    #plt.figure()
    #d.loc[:,col].dropna(axis=0,how='any').plot(style = 'o')
    #plt.savefig(col+'.png')

Fields = [x for _,x in alt.groupby('OBJECT')] #agrupar por objeto
#Lets see how many nights was used for each FIELD.
#for i in range(len(Fields)):

	#Field = str(Fields[i]['OBJECT'].unique())
	#Times_Observed = Fields[i]['NIGHT']
	#Nights_Observed = len(Times_Observed.unique())
	#print('Field: %a' % (Field))
	#print('Times Observed: %d'% (len(Times_Observed)))
	#print('Nights Observed: %d\n'% (Nights_Observed))
