import pandas as pd
import numpy as np
import subprocess


def moving_average(x, w):
  output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSSender.java'],stdout=subprocess.PIPE)
  num = output.stdout.read()
  df = pd.DataFrame(num)
  for i in range(0,df.shape[0]-2):
    df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()
    df.to_numpy().max()
    df.to_numpy().min()
    df.head()
