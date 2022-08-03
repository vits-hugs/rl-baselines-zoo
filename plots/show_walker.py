import  matplotlib.pyplot as plt
import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px
app = Dash(__name__)

path = "rl-baselines-zoo/control/sac/"
folder_name = "AntBulletEnv-v0_1/"
file = "0.monitor.csv"

exp_type = ['control','half','incremental']
todos=[]
for x in range(1,4):
    fig_a = []
    for name in exp_type:
        folder_name = f"Walker2DBulletEnv-v0_{x}/"
        path = f"rl-baselines-zoo/{name}/sac/"
        with open(path+folder_name+file,'r') as fin:
            data = fin.read().splitlines(True)
        if '#' in data[0]:
            with open(path+folder_name+file,'w') as fout:
                fout.writelines(data[1:])

        df = pd.read_csv(path+folder_name+file)
        fig = px.scatter(df, x="t", y="r",title=name)
        fig_a.append( dcc.Graph(
            id=folder_name+name,
            figure=fig
        ))
        fig_a.append( html.Div(className='spacer'))
    todos.append(html.Div([
    html.Div(className='row', children=[
        html.Div(className='parent', children=fig_a
        )
    ]),
]))
app.layout = html.Div(children=todos)

app.run_server(port=8051,debug=True)
