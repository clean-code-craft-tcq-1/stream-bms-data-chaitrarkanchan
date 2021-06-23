temperature_range = []
charge_rate = []
state_of_charge = []

def get_inputs(temp, cor, soc):
   temperature_range.append(temp)
   charge_rate.append(cor)
   state_of_charge.append(soc)
   return temperature_range, charge_rate, state_of_charge

def bms_min(bms_param):
   return min(bms_param)
   
def bms_max(bms_param):
   return max(bms_param)
  
def bms_movingaverage(bms_param):
   length = len(bms_param)
   if length >= 5:
      bmsmovingaverage = (sum(bms_param[-5:])/5)
      return bmsmovingaverage
   return "Invalid Count"
