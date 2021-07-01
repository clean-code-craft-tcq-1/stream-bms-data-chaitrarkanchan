temperature_range = []
state_of_charge = []
    
def get_inputs(temp,soc):
   temperature_range.append(temp)
   state_of_charge.append(soc)
   return temperature_range,state_of_charge

def bms_min_temp(temperature_range):
   return min(temperature_range)
   
def bms_max_temp(temperature_range):
   return max(temperature_range)

def bms_min_soc(state_of_charge):
   return min(state_of_charge)
   
def bms_max_soc(state_of_charge):
   return max(state_of_charge)
  
def bms_movingaverage(temperature_range,state_of_charge):
   length = len(state_of_charge)
   if length >= 5:
      bmsmovingaveragesoc = (sum(state_of_charge[-5:])/5)
      bmsmovingaveragetemp = (sum(temperature_range[-5:])/5)
      return bmsmovingaveragesoc,bmsmovingaveragetemp
   return "Invalid Count"

def displayoutput(temperature_range,state_of_charge):
    print("temperature",temperature_range)
    print("soc",state_of_charge)    
    print("MaximumTemp: ",bms_max_temp(temperature_range),"  MinimumTemp: ",bms_min_temp(temperature_range))
    print("MaximumSoc:  ",bms_max_soc(state_of_charge),"  MinimumSOC:  ",bms_min_soc(state_of_charge))
