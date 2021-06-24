
import subprocess
import pandas as pd

def bms_console_input():
    output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSSender.java'],stdout=subprocess.PIPE)
    inputdata = output.stdout.read()
    df = pd.DataFrame(inputdata)
    
    temperature_range = []
    state_of_charge = []
    
def get_inputs(temp,soc):
   temperature_range.append(temp)
   state_of_charge.append(soc)
   return temperature_range,state_of_charge
