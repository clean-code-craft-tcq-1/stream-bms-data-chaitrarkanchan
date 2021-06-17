import pandas as pd
import bms_sender_data

output = subprocess.check_output("java BMSServiceImpl", stderr=subprocess.PIPE)
numlist = BMSServiceImpl.paramValReading(5)
window_size = 3
num_series = pd.Series(numlist)
windows = num_series.rolling(window_size)

moving_averages = windows.mean()
moving_averages = moving_averages.tolist()
moving_averages_without_nans = moving_averages[window_size - 1:]

print(moving_averages_without_nans)
