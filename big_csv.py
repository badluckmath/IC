import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
#d = alt.pivot(columns='OBJECT',values='FILTER')
#d.iloc[:,:].plot(style = 'o', legend = False)
a = (alt.loc[:,'FILTER']== 625.4) &  (alt.loc[:,'ExpTime']==10.0)
alt.loc[a,'ExpTime'] =np.nan
alt.loc[a,'FILTER'] =np.nan
Fields = [x for _,x in alt.groupby('OBJECT')]
#Now, if you and to plot somenthing just write:
#Fields[x].loc[:,'FILTER'].plot(style = 'o', legend = True)
#plt.show()