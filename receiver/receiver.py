import pandas as pd
import subprocess

output =  subprocess.check_output(['java','-cp', 'src/main/java/BMSStreamSender/BMSServiceImpl.java'])
num = output.stdout.read()
print(num)
