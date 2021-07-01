
import json

def bms_console_readinput():
   try:
        input_data = input()
        data_list = json.loads(input_data)
        return process_values(data_list)             
    except EOFError:
        return None, None
        
def process_values(data_list):
    Temperature = data_list['Temperature']
    SOC = data_list['SOC']
    chargeRate = data_list['chargeRate'] 
    return Temperature, SOC
