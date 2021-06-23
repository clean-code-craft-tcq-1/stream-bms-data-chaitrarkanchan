
import subprocess
import pandas as pd

def bms_console_input():
    output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSSender.java'],stdout=subprocess.PIPE)
    inputdata = output.stdout.read()  
    df = pd.DataFrame(inputdata)
    temperature = df['temperature'].values
    soc = df['soc'].values
    charge_rate = df['chargeRate'].values
    return temperature, soc, charge_rate

