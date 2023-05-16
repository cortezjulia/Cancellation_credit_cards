
import pandas as pd
from IPython.display import display
import plotly.express as px

#import data
table=pd.read_csv('ClientesBanco.csv',encoding='latin1')
#delete useless column
table=table.drop('CLIENTNUM',axis=1)
display(table.round(1))

#Remove all rows wit NULL values from the DataFrame
table=table.dropna()

#displays the ratio of how many filled lines there are in each column
display(table.info())


#describes the distribution of each category in various parameters
display(table.describe().round(1))

#shows how many customers have the card and how many have canceled
category_quantity=table['Categoria'].value_counts()
display(category_quantity)
category_quantity_perc=table['Categoria'].value_counts(normalize=True)
display(category_quantity_perc)

#print graphics
for column in table:
    graphics=px.histogram(table,x=column,color='Categoria')
    graphics.show()

#Ratings extracted from the charts:

"""
--> the more contacts a customer makes, he will certainly cancel the card
--> most cancellations are Blue card
--> the more products the customer hires in the package, the lower the chances of cancellation
--> the smaller the financial movement and the fewer amounts moved, the greater the cancellation tendency
"""