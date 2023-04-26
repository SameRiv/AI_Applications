import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge as sk_Ridge

### Part 1 - Toy Dataset
""" example_data = {
    'Color': ['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'],
    'Has Wheels': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
    'Length (cm)': [24, 30, 50, 10, 15, 45],
    'Is Car': ['Yes', 'No', 'No', 'No', 'Yes', 'No'],
    'Owner Name': ['Charlie', 'Jim', 'Dolly', 'Medhi', 'Jessica', 'Alex'],
    'Owner Age': [12, 14, 8, 6, 11, 7]
}
toy_df = pd.DataFrame.from_dict(example_data)
toy_df.index = pd.Series([1, 4, 5, 7, 8, 12], name='Sample No.')
subset_df = toy_df.loc[4:8, 'Color']
#print(subset_df)
#print(toy_df) """

### Part 2 - Diabetes Dataset

##  setting up the Variables
diab_df=pd.read_csv("diabetes_cleaned.csv", sep=',',index_col=0)
target_col,feature_col=["target"],["s1","s2","s3","s4","s5","s6"]
metadata_col=["age","sex","bmi","bp","sample no."]
x,y,meta=diab_df.loc[:,feature_col], diab_df.loc[:,target_col], diab_df.loc[:,metadata_col]

##  Training
ml_model = sk_Ridge()
ml_model.fit(x, y)
predicted_list=ml_model.predict(x)

##  output
results_txt=""
for i in predicted_list:
    results_txt+=(str(i)+"\n")
with open ('Diabetes_Prediction.txt', 'w') as file:  
    file.write(results_txt) 