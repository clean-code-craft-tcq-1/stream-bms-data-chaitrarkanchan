import json

def read_sender_inputs():
    try:
        input_value = input()
        input_list = json.loads(input_value)
        print(input_list["Temperature"])
        print(input_list["SOC"])
        return input_list["Temperature"],input_list["SOC"]
    except EOFError:
        return None,None 
    
 class main():
    temperature_list = []
    soc_list = []
    
    while True:
        Temperature,soc=read_sender_inputs()
        if temperature == None or charge_rate == None:
            break
        temperature_list.append(Temperature)
        soc_list.append(SOC)
        print(temperature_list,soc_list)
