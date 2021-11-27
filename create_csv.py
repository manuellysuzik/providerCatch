import os
import pandas as pd

def create_dataframe(download:str, upload:str, ping:str , datetime:str, description:str):
  speedtest_results = pd.DataFrame()
  
  _data = {'Download': download, 'Upload': upload, 'Ping': ping, 'Description': description}
  
  test_df = pd.DataFrame([_data])
  test_df_DATETIME = pd.DataFrame([{'Datetime':datetime}])
  
  speedtest_results = pd.concat([test_df, test_df_DATETIME], axis=1, join='inner')
  print(speedtest_results)
  
  fileExists = os.path.isfile('data/speedtest_results.csv')
  
  if not fileExists:
    speedtest_results.to_csv('data/speedtest_results.csv', mode='w',header=['DOWNLOAD','UPLOAD','PING','SERVER','DATETIME'],index=False)
  else:
    speedtest_results.to_csv('data/speedtest_results.csv', mode='a', header=False, index=False)