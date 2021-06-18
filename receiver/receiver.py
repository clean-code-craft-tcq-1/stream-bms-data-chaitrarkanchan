import pandas as pd
import numpy as np
import subprocess


def moving_average(x, w):
  output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSServiceImpl.java'],stdout=subprocess.PIPE)
  num = output.stdout.read()
  df = pd.DataFrame(num)
  for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)
    df.head()
