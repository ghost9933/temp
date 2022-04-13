# use environment file to import
# from tkinter.tix import COLUMN
import glob
import os
import zipfile
from datetime import datetime
import env
import pandas as pd
#load data from the path to a data fr
dfs = []
for filename in os.listdir(env.srcpath):
    if filename.endswith('.zip'):
        zip_file = os.path.join(env.srcpath, filename)
        zf = zipfile.ZipFile(zip_file)
        dfs += [pd.read_csv(zf.open(f),names=env.btcusdt_h) for f in zf.namelist()]
        print 
df = pd.concat(dfs,axis=0,ignore_index=True)

# typecast the timestamp to date time
df['Timestamp']= pd.to_datetime(df['Timestamp'],unit = 'ms')

print(df)
