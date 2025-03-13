from fasthtml.common import *
from monsterui.all import *

from app.models import get_all

header_data = ['equipo', 'id_equipo', 'descripcion', 'id_variable']

def definir_tabla(tabla_id, Titulo_tabla):
    tabla_def = Section(
        H2(Titulo_tabla),
        tabla_id,
        cls="my-6")
    return(tabla_def)

def table_valores(body_data):
    return definir_tabla(TableFromDicts(header_data, body_data, 
        header_cell_render=lambda v: Th(v.upper())), "Tabla de Valores")

def pagina_final():
    valores = get_all()
    return Title("Variables"), Container(
            H2("Variables de la instalación"),
            DivRAligned(
                Button("Volver", cls=ButtonT.primary, hx_post="/volver",),
            ), 
            table_valores(valores),
            Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
            cls=('space-y-4', ContainerT.xl)
        )