import  matplotlib.pyplot as plt
import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px
import plotly.subplots as tls
app = Dash(__name__)

path = "control/"
folder_name = ""
file = "ant_control.csv"

exp_type = ['control','half','incremental']

df = pd.read_csv(path+folder_name+file)
df_2 = pd.read_csv("half/"+file)
df_3 = pd.read_csv("incremental/"+file)
fig = tls.make_subplots(rows=1, cols=3, shared_yaxes=True,vertical_spacing=0.009,horizontal_spacing=0.009)
fig['layout']['margin'] = {'l': 30, 'r': 10, 'b': 50, 't': 25}

fig.append_trace({'y':df.r,'type':'box','name':'Price'},1,1)
fig.append_trace({'y':df_2.r,'type':'box','name':'half'},1,2)
fig.append_trace({'y':df_3.r,'type':'box','name':'incremental'},1,3)
#fig = px.box(df,y="r",title="title")
app.layout = html.Div(children=[dcc.Graph(
    id="hardcoda",
    figure=fig
)])

app.run_server(port=8051,debug=True)
