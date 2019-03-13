import pandas as pd
import plotly as py
import plotly.graph_objs as pygo
import numpy as np
from plotly.graph_objs import Scatter, Layout, Data

trace0 = Scatter(
    mode='lines+markers',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[10, 12, 15, 13, 14, 12, 9, 11, 13, 12, 14, 15],
    line = dict(shape='spline'),
    text = 'This is a text',textposition='top right')
trace1 = Scatter(
    mode='markers',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[13, 12, 11, 10, 8, 9, 12, 14, 15, 14, 13, 12])
trace2 = Scatter(
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[-2, -3, -1, 0, 1, 2, 3, 6, 7, 6, 5, 4], mode='lines',
    name='This is a name')
trace3 = Scatter(
    mode='lines',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[14, 16, 19, 18, 20, 21, 22, 24, 23, 20, 18, 19],
    line=dict(dash = 'dot'))                                #'solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot'
trace4 = Scatter(
    mode='lines',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[12, 14, 18, 20, 24, 26, 27, 29, 30, 29, 28, 28],
    line = dict(width=4,color='rgb(23,45,56)'))
trace5 = Scatter(
    mode='markers',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[23, 24, 25, 26, 27, 29, 31, 32, 29, 26, 23, 22], 
    marker = dict(size=12,color='rgb(200,125,240)'))
trace6 = Scatter(
    mode='lines',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[33, 32, 30, 31, 33, 34, 36, 35, 33, 32, 30, 31], 
    opacity=0.3,
    name = 'This is an other name')
trace7 = Scatter(
    mode='markers',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[40, 41, 39, 38, 39, 40, 42, 44, 45, 44, 40, 41], 
    marker = dict(size=[40/2, 41/2, 39/2, 38/2, 39/2, 40/2, 42/2, 44/2, 45/2, 44/2, 40/2, 41/2]))

trace8 = Scatter(
    mode='markers',
    x=[-100, 000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 
    y=[32, 31, 30, 28, 29, 31, 33, 36, 35, 34, 33, 34], 
    #marker = dict(color=[0, 50],showscale=True)
)

trace9 = Scatter(
    mode='lines',
    x = np.loadtxt('FullDATA.dat',usecols=(0), unpack=True),
    y = (np.loadtxt('FullDATA.dat',usecols=(1), unpack=True))*300000000,
    )

data = Data([trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9])

fig = dict(data=data)
py.plot(fig, filename='Offline2DBasic')