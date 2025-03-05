import requests
import json
import pandas as pd

from app.config import settings

token_vrm = "Token " + settings.VRM_TOKEN
instalacion = settings.VRM_Instalacion
url_vrm = "https://vrmapi.victronenergy.com/v2/installations/" + instalacion
headers = { "Content-Type": "application/json","x-authorization": token_vrm}

def Consultar_variables():
    url = url_vrm + "/diagnostics"
    response = requests.request("GET", url, headers=headers)
    valores = json.loads(response.text)
    valor_ref = []
    for i in range(len(valores['records'])):
        valor_ref.append({'instalacion': instalacion, 'equipo': valores['records'][i]['Device'], 'id_equipo': valores['records'][i]['instance'], 
               'descripcion': valores['records'][i]['description'], 'id_variable' : valores['records'][i]['idDataAttribute']})
    df = pd.DataFrame.from_dict(valor_ref) 
    return(df)

def BatterySummary():
    url = url_vrm + "/widgets/BatterySummary"
    querystring = {"instance":"512"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    valores = json.loads(response.text)
    batterySoC = float(valores['records']['data']['51']['value'])
    batteryVolt = float(valores['records']['data']['47']['value'])
    batteryInt = float(valores['records']['data']['49']['value'])
    batteryTemp = float(valores['records']['data']['115']['value'])
    batteryAlarmLowVolt = valores['records']['data']['119']['value']
    batteryAlarmHighVolt = valores['records']['data']['120']['value']
    batteryAlarmLowTemp = valores['records']['data']['124']['value']
    batteryAlarmHighTemp = valores['records']['data']['125']['value']
    batteryMinCellVolt = float(valores['records']['data']['173']['value'])
    batteryMaxCellVolt = float(valores['records']['data']['174']['value'])
    valores = {'batterySoC': batterySoC, 'batteryVolt': batteryVolt, 'batteryInt': batteryInt, 'batteryTemp': batteryTemp,
        'batteryMinCellVolt': batteryMinCellVolt, 'batteryMaxCellVolt': batteryMaxCellVolt,
        'Alarms': {
            'batteryAlarmLowVolt': batteryAlarmLowVolt, 'batteryAlarmHighVolt': batteryAlarmHighVolt, 
            'batteryAlarmLowTemp': batteryAlarmLowTemp, 'batteryAlarmHighTemp': batteryAlarmHighTemp}}
    return(valores)

def SolarChargerSummary():
    url = url_vrm + "/widgets/SolarChargerSummary"
    querystring = {"instance":"256"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    valores = json.loads(response.text)
    phVolt = float(valores['records']['data']['81']['value'])
    phState = valores['records']['data']['85']['value']
    phRealay = valores['records']['data']['90']['value']
    phYield = float(valores['records']['data']['94']['value'])
    batPower = float(valores['records']['data']['107']['value'])
    valores = {'phVolt': phVolt, 'phState': phState, 'phRealay': phRealay, 'phYield': phYield,
        'batPower': batPower}
    return(valores)

def SystemSummary():
    url = url_vrm + "/installations/105393/widgets/Status"
    querystring = {"instance":"0"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    valores = json.loads(response.text)
    V1_IN = float(valores['records']['data']['8']['value'])
    I1_IN = float(valores['records']['data']['11']['value'])
    PA1_IN = float(valores['records']['data']['17']['value'])
    V1_OUT = float(valores['records']['data']['20']['value'])
    I1_OUT = float(valores['records']['data']['23']['value'])
    PA1_OUT = float(valores['records']['data']['29']['value'])
    V_DC = float(valores['records']['data']['32']['value'])
    I_DC = float(valores['records']['data']['33']['value'])
    State = valores['records']['data']['40']['value']
    Temp = float(valores['records']['data']['521']['value'])
    valores = {'V1_IN': V1_IN, 'I1_IN': I1_IN, 'PA1_IN': PA1_IN,
        'V1_OUT': V1_OUT, 'I1_OUT': I1_OUT, 'PA1_OUT': PA1_OUT,
        'V_DC': V_DC, 'I_DC': I_DC, 'State': State, 'Temp': Temp}
    return(valores)