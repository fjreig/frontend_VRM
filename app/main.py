from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from monsterui.all import *
from datetime import datetime
import pandas as pd

from app.api import Consultar_variables
from app.models import new_register_variable, get_id_variable, new_registers
from app.table import pagina_final
from app.form import generar_formularuio
from app.dashboard import generate_chart, get_data_api, generate_report

hdrs = (Theme.blue.headers())
app, rt = fast_app(hdrs=hdrs)

@dataclass
class new_charts:
    equipo: str
    variable: str
    fecha_inicio: str
    fecha_final: str

@rt('/')
def index():
    formulario = generar_formularuio()
    return(formulario)

@rt('/volver')
def post():
    return Redirect("/")

@rt('/tabla')
def tabla():
    return(pagina_final())

@rt("/new_chart")
def post(grafica: new_charts):
    valores = grafica.__dict__
    return Redirect(f"/grafica/{valores['equipo']}/{valores['variable']}/{valores['fecha_inicio']}/{valores['fecha_final']}")

@rt("/new_report")
def post(grafica: new_charts):
    valores = grafica.__dict__
    return Redirect(f"/report/{valores['equipo']}/{valores['variable']}/{valores['fecha_inicio']}/{valores['fecha_final']}")

@rt("/new_download")
def post(grafica: new_charts):
    valores = grafica.__dict__
    return Redirect(f"/obtener/{valores['equipo']}/{valores['variable']}/{valores['fecha_inicio']}/{valores['fecha_final']}")

@rt("/grafica/{equipo}/{variable}/{fecha_inicio}/{fecha_final}")
def get(equipo: str, variable: str, fecha_inicio: str, fecha_final: str):
    valores = get_id_variable(equipo, variable)
    df = get_data_api(fecha_inicio, fecha_final, valores)
    return Title("Graficas"), Container(
            H2("Graficas"),
            DivRAligned(
                Button("Volver", cls=ButtonT.primary, hx_post="/volver",),
            ), 
            Grid(
                Card(
                    Safe(generate_chart(df, variable, valores['id_variable'])), cls='col-span-4',
                header=Div(CardTitle(variable))),
            ),
            Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
            cls=('space-y-4', ContainerT.xl)
        )

@rt("/report/{equipo}/{variable}/{fecha_inicio}/{fecha_final}")
def get(equipo: str, variable: str, fecha_inicio: str, fecha_final: str):
    valores = get_id_variable(equipo, variable)
    df = get_data_api(fecha_inicio, fecha_final, valores)
    return Title("Informe"), Container(
            H2("Informe"),
            DivRAligned(
                Button("Volver", cls=ButtonT.primary, hx_post="/volver",),
            ), 
            generate_report(df),
            Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
            cls=('space-y-4', ContainerT.xl)
        )

@rt("/obtener/{equipo}/{variable}/{fecha_inicio}/{fecha_final}")
def get(equipo: str, variable: str, fecha_inicio: str, fecha_final: str):
    try:
        valores = get_id_variable(equipo, variable)
        df = get_data_api(fecha_inicio, fecha_final, valores)
        df.rename(columns={df.columns[1]: variable}, inplace=True)
        df = pd.melt(df, id_vars=['fecha'], value_vars=variable)
        new_registers(df)
        print("OK")
    except:
        print("NOK")
    return Redirect("/")

@rt('/variables')
def index():
    try:
        valores = Consultar_variables()
        new_register_variable(valores)
        print("OK")
    except:
        print("NOK")
    return Redirect("/")

serve()