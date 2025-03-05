from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
import pandas as pd
import datetime
import json

from app.config import settings
from app.database import Base, session, engine

instalacion = settings.VRM_Instalacion

class Variables_lista(Base):
    __tablename__ = "variables"

    #id = Column(Integer, primary_key=True, index=True)
    instalacion = Column(String, primary_key=True)
    equipo = Column(String, primary_key=True)
    id_equipo = Column(Integer)
    descripcion = Column(String)
    id_variable = Column(Integer, primary_key=True)

## Añadir nuevos registros
def new_register_variable(df):
    valores = df.to_dict('records')
    for i in range(len(valores)):
        registro = Variables_lista(
            instalacion = instalacion,
            equipo = valores[i]['equipo'],
            id_equipo = valores[i]['id_equipo'],
            descripcion = valores[i]['descripcion'],
            id_variable = valores[i]['id_variable'],
        ) 
        session.add(registro)
        session.commit()

def get_all():
    result = session.query(Variables_lista).all()
    df = pd.DataFrame([r.__dict__ for r in result])
    df = df.drop(columns=['_sa_instance_state'])
    df = df.reset_index()
    valores = df.to_dict('records')
    return(valores)

def get_equipos():
    result = session.query(Variables_lista).distinct(Variables_lista.equipo).all()
    df = pd.DataFrame([r.__dict__ for r in result])
    df = df.drop(columns=['_sa_instance_state', 'id_variable', 'descripcion'])
    valores = df.to_dict('records')
    return(valores)