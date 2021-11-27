import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

def internet_graphs():
  
  data = pd.read_csv('data/speedtest_results.csv', header=0)
  
  ping = data.get('PING')
  download = data.get('DOWNLOAD')
  upload = data.get('UPLOAD')

  download_mean = np.mean(download)
  upload_mean = np.mean(upload)
  ping_mean = np.mean(ping)
  
  plt.style.use('ggplot')
  x_pi = len(ping)
  
  tests = np.linspace(0, x_pi, x_pi)
  
  fig1, ax1 = plt.subplots(figsize=(10,5))
  fig2, ax2 = plt.subplots(figsize=(10,5))
  fig3, ax3 = plt.subplots(figsize=(10,5))
  
  ax1.plot(tests, download, color='r',
           label='Download Speed Media: {:.2f} MB/s'
           .format(download_mean))
  ax1.set(xlabel="Test", ylabel="Download Speed in MB/s",)
  ax1.legend(loc='best')
  
  ax2.plot(tests, upload, color='g',
           label='Upload Speed Media: {:.2f} MB/s'.format(upload_mean))
  ax2.set(xlabel="Test", ylabel="Upload Speed in MB/s",)
  ax2.legend(loc='best')
  
  ax3.plot(tests, ping, color='m',label='Ping Media : {:.2f} ms'.format(ping_mean))
  ax3.set(xlabel="Test", ylabel="Ping (ms)")
  ax3.legend(loc='best')
  
  fig1.savefig('data/img/Download')
  fig2.savefig('data/img/Upload')
  fig3.savefig('data/img/Ping')
  
  plt.show()
  print('Gerando gráficos...\n')
  
internet_graphs()