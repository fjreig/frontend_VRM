from fasthtml.common import *
from fasthtml.components import Uk_input_tag
from fasthtml.svg import *
from monsterui.all import *

from app.models import get_equipos, get_variables_from_equipo

equipos = get_equipos()

def Generar_Card(variables, titulo):
    ReportIssue = Card(
        Form(
            Grid(
                Div(LabelInput('Euipo', id='equipo', value=titulo, name="equipo", readonly=True)), 
            ),
            Grid(
                Div(LabelSelect(*Options(*variables), label='variable', id='variable', name='variable'))
            ),
            Grid(LabelInput("Fecha Inicio",id='fecha_inicio', type="date", name='fecha_inicio'),
                LabelInput("Fecha Final",id='fecha_final', type="date", name='fecha_final')),
            DivLAligned(
                Button("Grafica", cls=ButtonT.primary, hx_post="/new_chart"),
                Button("Informe", cls=ButtonT.primary, hx_post="/new_report"),
                Button("Descarga", cls=ButtonT.primary, hx_post="/new_download")
            ),
        ),
        header=(H3(f'Equipo {titulo}')))
    return(ReportIssue)

def Generar_formularios():
    formularios = []
    for i in range(len(equipos)):
        nombre_equipo = equipos[i]
        formularios.append(Generar_Card(get_variables_from_equipo(nombre_equipo), nombre_equipo))
    return(formularios)

def generar_formularuio():
    valores = Generar_formularios()
    col1 = Div(valores[0], valores[3], cls='space-y-4')
    col2 = Div(valores[1], valores[4], cls='space-y-4')
    col3 = Div(valores[2], cls='space-y-4')
    return Title("VRM"), Container(
            H2("VRM Portal"),
            DivRAligned(
                Button("Volver", cls=ButtonT.primary, hx_post="/volver",),
            ), 
            Grid(
                *map(Div,(col1, col2, col3)), cols_md=1, cols_lg=2, cols_xl=3
            ),
            Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
            cls=('space-y-4', ContainerT.xl)
        )