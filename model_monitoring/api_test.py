import requests
import pandas as pd
import time

df=pd.read_csv('./Fake-data/fake.csv')
df = df.iloc[: , 1:]
test_values=df.values
print(test_values)
print(test_values)

url = 'http://localhost:8000/api/v1/'

for i in test_values:
    list_1 = i.tolist()
    myobj = {"X": list_1}
    print(len(list_1))
    print(myobj)
    
# myobj = {'somekey': 'somevalue'}


    
    x = requests.post(url, json = myobj)
   # time.sleep(3)

    print(x.text)