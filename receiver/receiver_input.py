
import json
import pandas as pd

def bms_console_input():
    inputdata = input()   
    df = pd.DataFrame(inputdata)
    temperature = df['temperature'].values
    soc = df['soc'].values
    charge_rate = df['chargeRate'].values
    return temperature, soc, charge_rate

