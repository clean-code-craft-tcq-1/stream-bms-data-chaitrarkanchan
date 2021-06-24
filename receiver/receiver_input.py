
import sys
import ast

def bms_console_input():
  data = sys.stdin.readlines()    
  for i in data:
    bms_param_data = ast.literal_eval(data)
    Temperature = bms_param_data['Temperature']
    Soc = bms_param_data['Soc']
    return Temperature, Soc
        
    
