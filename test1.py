import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go



py.plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='C:\\Users\Administrator\Desktop\my-graph.html',image='jpeg')