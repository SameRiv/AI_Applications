import pandas as pd
import numpy as np
iris_df = pd.read_csv("iris_full.csv",sep=',',index_col=0)
#print(iris_df.columns)
#print(iris_df.shape)
print(iris_df.loc[:,'petal length (cm)'].mean())
