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
print(moving_averages_without_nans)
print ("Max number:",max(numlist), "\nMin number:",min(numlist))
