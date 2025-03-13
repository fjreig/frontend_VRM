from fasthtml.common import *
import fasthtml.common as fh
from monsterui.all import *
from fasthtml.svg import *
import plotly.express as px
from datetime import datetime

from app.api import Grafica

def generate_chart(df, titulo_eje_y, variable):  
    fig = px.line(df, x='fecha', y=str(variable),  template='plotly_white', line_shape='spline')
    fig.update_traces(mode='lines')
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), hovermode='x unified',
        showlegend=True, legend=dict(orientation='h', yanchor='bottom', y=1.02,  xanchor='right', x=1),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showline=True, linewidth=1, linecolor='white', gridcolor='rgba(0,0,0,0)'),
        yaxis=dict(showline=True, linewidth=1, linecolor='white', gridcolor='rgba(0,0,0,0)'))
    fig.update_layout(xaxis_title="Fecha", yaxis_title=titulo_eje_y)
    fig.update_yaxes(title_font_color="white", color="white", rangemode="tozero")
    fig.update_xaxes(title_font_color="white", color="white")
    return fig.to_html(include_plotlyjs=True, full_html=False, config={'displayModeBar': False})

def get_data_api(fecha_inicio, fecha_final, valores):
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_final = datetime.strptime(fecha_final, '%Y-%m-%d')
    df = Grafica(fecha_inicio, fecha_final, valores['id_equipo'], valores['id_variable'])
    return(df)

def generate_report(df):
    header_data = list(df.columns)
    body_data = df.to_dict('records')    
    return TableFromDicts(header_data, body_data)