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
  
def print_to_console(): 
    print('MaximumTemperature', bms_max(temperature_range))
    print('MinimumTemperature', bms_min(temperature_range))
    print('MovingAvg', bms_movingaverage(temperature_range))
    print('MaximumSOC', bms_max(state_of_charge))
    print('MinimumSOC', bms_min(state_of_charge))
    print('MovingAvgSOC', bms_movingaverage(state_of_charge))
    print('MaximumChargeRate', bms_max(charge_rate))
    print('MinimumChargeRate', bms_min(charge_rate))
    print('MovingAvgChargeRate', bms_movingaverage(charge_rate))
    
    
