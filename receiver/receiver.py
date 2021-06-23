
import sys
import pandas as pd

def bms_console_input():
    data = sys.stdin.readlines()
    input_data = ''
    
    #get the streaming data from java console output in the pipeline
    for line in data:
        if 'temperature' in line:
            input_data = line
            
def moving_average(x, w):
    df = pd.DataFrame(input_data)
    for i in range(0,df.shape[0]-2):
      df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()
      df.to_numpy().max()
      df.to_numpy().min()
      df.head()
