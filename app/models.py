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

class Variables_registro(Base):
    __tablename__ = "registros"

    instalacion = Column(String, primary_key=True)
    fecha = Column(DateTime, primary_key=True)
    variable = Column(String, primary_key=True)
    valor = Column(Float)

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

def new_registers(df):
    valores = df.to_dict('records')
    for i in range(len(valores)):
        registro = Variables_registro(
            instalacion = instalacion,
            fecha = valores[i]['fecha'],
            variable = valores[i]['variable'],
            valor = valores[i]['value'],
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
    #df = df.drop(columns=['_sa_instance_state', 'id_variable', 'descripcion','instalacion', 'id_equipo'])
    #valores = df.to_dict('records')
    valores = df['equipo'].tolist()
    return(valores)

def get_variables_from_equipo(equipo_consulta):
    result = session.query(Variables_lista).filter(Variables_lista.equipo == equipo_consulta).all()
    df = pd.DataFrame([r.__dict__ for r in result])
    valores = df['descripcion'].tolist()
    return(valores)

def get_id_variable(equipo_consulta, variable_consulta):
    result = session.query(Variables_lista).filter(Variables_lista.equipo == equipo_consulta, Variables_lista.descripcion == variable_consulta).all()
    df = pd.DataFrame([r.__dict__ for r in result])
    df = df.drop(columns=['_sa_instance_state', 'instalacion'])
    valores = df.to_dict('records')
    return(valores[0])