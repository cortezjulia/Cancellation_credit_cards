

import pandas as pd
from IPython.display import display
import plotly.express as px

table=pd.read_csv('ClientesBanco.csv',encoding='latin1')
table=table.drop('CLIENTNUM',axis=1)
display(table.round(1))


table.dropna()
display(table.info())

display(table.describe().round(1))
category_quantity=table['Categoria'].value_counts()
display(category_quantity)
category_quantity_perc=table['Categoria'].value_counts(normalize=True)
display(category_quantity_perc)

for column in table:
    grafico=px.histogram(table,x=column,color='Categoria')
    grafico.show()


