import  matplotlib.pyplot as plt
import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px
app = Dash(__name__)

path = "rl-baselines-zoo/control/sac/"
folder_name = "AntBulletEnv-v0_1/"
file = "0.monitor.csv"

fig_a = []
for x in range(1,6):
    folder_name = f"HopperBulletEnv-v0_{x}/"
    with open(path+folder_name+file,'r') as fin:
        data = fin.read().splitlines(True)
    if '#' in data[0]:
        with open(path+folder_name+file,'w') as fout:
            fout.writelines(data[1:])

    df = pd.read_csv(path+folder_name+file)
    fig = px.scatter(df, x="t", y="r",title=folder_name)
    fig_a.append( dcc.Graph(
        id=folder_name,
        figure=fig
    ))


app.layout = html.Div(children=fig_a)

app.run_server(debug=True)
