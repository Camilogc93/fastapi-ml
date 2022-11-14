import sweetviz as sv
import pandas as pd

from sdv.tabular import GaussianCopula
df=pd.read_csv('./datasets/train.csv',index_col=None)
print(df)
print(df.shape)
df = df.iloc[: , 1:]
print(df.shape)
model = GaussianCopula()
model.fit(df)
sample = model.sample(2000)

sample.to_csv("./Fake-data/fake.csv")
analysis = sv.analyze(sample)
analysis.show_html()