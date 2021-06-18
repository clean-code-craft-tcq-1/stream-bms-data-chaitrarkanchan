import pandas as pd
import subprocess

output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSServiceImpl.java'],stdout=subprocess.PIPE)
num = output.stdout.read()
numlist = pd.to_numeric(num)
window_size = 3
num_series = pd.Series(numlist)
windows = num_series.rolling(window_size)

moving_averages = windows.mean()
moving_averages = moving_averages.tolist()
moving_averages_without_nans = moving_averages[window_size - 1:]

def max_temp(numlist):
    maximumtemp = max(numlist)
    print(maximumtemp) 
      
def min_temp(numlist):
    minimumtemp = min(numlist) 
    print(minimumtemp)

def max_soc(numlist):
    maximumsoc = max(numlist)
    print(maximumsoc)

def min_soc(numlist):
    minimumsoc = min(numlist)
    print(minimumsoc)

print(moving_averages_without_nans)
print("MaxTemp - ",max_temp(numlist),"  MinTemp - ",min_temp(numlist))
print("MaxSOC -  ",max_soc(numlist),"  MinSOC -  ",min_soc(numlist))
