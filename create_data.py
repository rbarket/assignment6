import pandas as pd
import numpy as np
import time
from implementations import all_implementations

df=pd.DataFrame()

samples = 45
timestart = time.time()
for sort in all_implementations:
    
    tests = []
    for trial in range(samples):
        random_array=np.random.randint(100000, size=(20000))
        st = time.time()
        res = sort(random_array)
        en = time.time()
        timer = en-st
        tests.append(timer)
        col = pd.Series(tests).rename(str(sort))
    df = pd.concat([df,col], axis=1)
timeend = time.time()
totaltime = timeend-timestart
df.to_csv('data.csv', index=False)
