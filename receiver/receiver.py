import pandas as pd
import subprocess
import BMSServiceImpl


output = subprocess.check_output("java BMSServiceImpl", stderr=subprocess.PIPE)
numlist = BMSServiceImpl.paramValReading(10)
window_size = 3
num_series = pd.Series(numlist)
windows = num_series.rolling(window_size)

moving_averages = windows.mean()
moving_averages = moving_averages.tolist()
moving_averages_without_nans = moving_averages[window_size - 1:]

def max_temp(numlist):
    return max(numlist)
      
def min_temp(numlist):
    return min(numlist) 

def max_soc(numlist):
    return max(numlist)  

def min_soc(numlist):
    return min(numlist)

print(moving_averages_without_nans)
print("MaxTemp - ",max_temp(numlist),"  MinTemp - ",min_temp(numlist))
print("MaxSOC -  ",max_soc(numlist),"  MinSOC -  ",min_soc(numlist))
    