import os
import pandas as pd
import plotly
import plotly.io as po
import plotly.plotly as py
import numpy as np
from plotly.graph_objs import *
from plotly.offline import *

trace0 = Scatter(
    mode='lines',
    x = np.loadtxt('FullDATA0.dat',usecols=(0), unpack=True),
    y = (np.loadtxt('FullDATA0.dat',usecols=(1), unpack=True))*1,
    line = dict(shape='linear'),)
trace1 = Scatter(
    mode='lines',
    x = np.loadtxt('FullDATA1.dat',usecols=(0), unpack=True),
    y = (np.loadtxt('FullDATA1.dat',usecols=(1), unpack=True))*1,
    line = dict(shape='linear'),)
trace2 = Scatter(
    mode='lines',
    x = np.loadtxt('FullDATA2.dat',usecols=(0), unpack=True),
    y = (np.loadtxt('FullDATA2.dat',usecols=(1), unpack=True))*1000,
    line = dict(shape='linear'),)

data = Data([trace0,trace1,trace2])

layout = dict(
    title = 'This is a Title',
    font = dict (family='Serif', size = 16),
    xaxis = dict (title='Title of X-Axis', zeroline=False, showgrid=True, showline=True, mirror='ticks', linewidth=1.2, ticks='inside', range=[-10,200]),
    yaxis = dict (title='Title of Y-Axis', zeroline=False, showgrid=True, showline=True, mirror='ticks', linewidth=1.2, ticks='inside',),
    showlegend=True,
    legend = dict (x=0.75, y=0.6),
)

if not os.path.exists('images'):
    os.mkdir('images')

fig = dict(data=data, layout=layout)
plotly.offline.plot(data, filename = 'Offline2DDATA.html')
#py.plot(fig, filename='Offline2DDATA')
po.write_image(fig, 'images/Offline2DDATAorca.pdf')
py.image.save_as(fig, 'Offline2DDATA.png')
#py.image.save_as(fig, 'Offline2DDATA.pdf')
