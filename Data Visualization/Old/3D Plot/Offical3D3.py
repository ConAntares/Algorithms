import os
import pandas as pd
import plotly
import plotly.io as pio
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/vortex.csv")

data = [{
    "type": "cone",
    "x": df['x'],
    "y": df['y'],
    "z": df['z'],
    "u": df['u'],
    "v": df['v'],
    "w": df['w'],
    "colorscale": 'Blues',
    "sizemode": "absolute",
    "sizeref": 40
}]

layout = {
    "scene": {
        "aspectratio": {"x": 1, "y": 1, "z": 0.8},
        "camera": {
            "eye": {"x": 1.2, "y": 1.2, "z": 0.6}
        }
    }
}

if not os.path.exists('images'):
    os.mkdir('images')

fig = {"data": data, "layout": layout}
py.plot(fig, filename="cone-vortex", validate=False)
pio.write_image(fig, 'images/cone-vortex.pdf')
