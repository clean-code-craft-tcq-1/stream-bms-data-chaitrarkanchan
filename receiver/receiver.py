
import sys
import pandas as pd

def bms_console_input():
    incoming_values = sys.stdin.readlines()
    input = ''
    
    for range in incoming_values:
        if 'temperature' in range:
            input = range
            
    df = pd.DataFrame(input)
    for i in range(0,df.shape[0]-2):
      df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()
      df.to_numpy().max()
      df.to_numpy().min()
      df.head()
