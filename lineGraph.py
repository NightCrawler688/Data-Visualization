import pandas as pd
import plotly_express as px 
#df is creating a data frame using panda module and is using a csv file
df = pd.read_csv("line_chart.csv")
#print(df)
fig = px.line(df,x = 'Year',y = 'Per capita income',color = 'Country',title = 'Per Capita Income')
fig.show()
