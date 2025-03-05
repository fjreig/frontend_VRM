from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from monsterui.all import *
from datetime import datetime
import pandas as pd

from app.api import Consultar_variables
from app.models import new_register_variable, get_equipos
from app.table import pagina_final

hdrs = (Theme.blue.headers())
app, rt = fast_app(hdrs=hdrs)

@rt('/')
def index():
    equipos = get_equipos()
    print(equipos)
    return(H1("Hola"))

@rt('/tabla')
def tabla():
    return(pagina_final())

@rt('/variables')
def index():
    try:
        valores = Consultar_variables()
        new_register_variable(valores)
        return(H1("OK"))
    except:
        return(H1("NOK"))

serve()