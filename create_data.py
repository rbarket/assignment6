import pandas as pd
import numpy as np
import time
from implementations import all_implementations

df=pd.DataFrame()

samples = 55
timestart = time.time()
names=['qs1','qs2','qs3','qs4','qs5','merge1','partition']
for i in range(len(all_implementations)):
    print(f'test {names[i]}')
    tests = []
    for trial in range(samples):
        random_array=np.random.randint(100000, size=(12250))
        st = time.time()
        res = all_implementations[i](random_array)
        en = time.time()
        timer = en-st
        tests.append(timer)
        col = pd.Series(tests).rename(names[i])
    df = pd.concat([df,col], axis=1)
timeend = time.time()
totaltime = timeend-timestart
print(totaltime)
df.to_csv('data.csv', index=False)
