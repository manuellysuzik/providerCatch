
import time
import speedtest
from create_csv import create_dataframe

st = speedtest.Speedtest()

server = st.get_best_server()
test_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
description = f"{server['sponsor']} - Location:{server['name']}/{server['country']}"
download = '{:.2f}'.format(st.download()/(10 ** 6))
upload = '{:.2f}'.format(st.upload()/(10 ** 6))
ping = '{:.2f}'.format(st.results.ping)
create_dataframe(download, upload,ping, test_datetime , description)

