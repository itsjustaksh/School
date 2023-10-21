import numpy as np
import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("202212-citibike-tripdata.csv")
relData = df[['started_at', 'ended_at', 'member_casual']]

for i in range(len(relData[['started_at']])):
    relData.at[i, 'started_at'] = dt.strptime(relData['started_at'][i], "%Y-%m-%d %H:%M:%S")
    relData.at[i, 'ended_at'] = dt.strptime(relData['ended_at'][i], "%Y-%m-%d %H:%M:%S")

print(relData['started_at'][2])
