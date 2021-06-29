import json

def read_sender_inputs():
    try:
        input_value = input()
        input_list = json.loads(input_value)
        print(input_list)   
        return input_list["Temperature"],input_list["SOC"]
    except EOFError:
        return None,None 
