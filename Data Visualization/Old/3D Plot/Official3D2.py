import os
import pandas as pd
import plotly
import plotly.io as pio
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-basic.csv')

data = [go.Streamtube(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    u = df['u'],
    v = df['v'],
    w = df['w'],
    sizeref = 0.5,
    colorscale = 'Blues', 
    cmin = 0,
    cmax = 3
    )
]

layout = go.Layout(
    scene = dict(
      camera = dict(
        eye = dict(
          x = -0.7243612458865182,
          y = 1.9269804254717962,
          z = 0.6704828299861716
        )
      )
    )
)

if not os.path.exists('images'):
    os.mkdir('images')
    
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='streamtube-basic')
pio.write_image(fig, 'images/streamtube-basic.pdf')
