import  matplotlib.pyplot as plt
import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px
app = Dash(__name__)

path = "control/"
folder_name = ""
file = "ant_control.csv"

exp_type = ['control','half','incremental']

df = pd.read_csv(path+folder_name+file)
fig = px.box(df,y="r",title="title")
app.layout = html.Div(children=[dcc.Graph(
    id="hardcoda",
    figure=fig
)])

app.run_server(port=8051,debug=True)
