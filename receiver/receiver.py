import numpy as np
import subprocess


def moving_average(x, w):
  output = subprocess.Popen(['java','-cp', 'src/main/java/BMSStreamSender/BMSServiceImpl.java'],stdout=subprocess.PIPE)
  num = output.stdout.read()
  return np.convolve(x, np.ones(w), 'valid') / w

data = np.array(num)

print(moving_average(data,4))
print ("Max number:",max(data), "\nMin number:",min(data))
