####                           before running the code,                          ####
###                              Put iris_full.csv in                             ###
##                                 the script's Dir.                               ##

import pandas as pd
from sklearn.preprocessing import normalize as sk_normalize
from sklearn.linear_model import LogisticRegression as sk_LogisticRegression

### reading CSV
iris_df=pd.read_csv("iris_full.csv", sep=',',index_col=0)
target_col,metadata_col=["species"],["collecting researcher"]
feature_col=["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"]

### setting x,y,meta variables
x,y,meta=iris_df.loc[:,feature_col], iris_df.loc[:,target_col], iris_df.loc[:,metadata_col]

### normalization
x_normed=sk_normalize(x,norm='l2',axis=1)
x.loc[:,:]=x_normed

### Learning
log_model=sk_LogisticRegression(penalty=None)
log_model.fit(x,y)

### checking accuracy and creating output
predicted_list=log_model.predict(x)
realValues_list=y["species"].values.tolist()
results_txt, total_count, correct_pred_count = "", len(predicted_list), 0

for i in range(total_count):
    pred_item, real_item = predicted_list[i], realValues_list[i]
    if pred_item==real_item:
        results_txt+=(str(pred_item)+"\t"+"Correct!"+"\n")
        correct_pred_count += 1
    else:
        results_txt+=(str(pred_item)+"\t"+"Incorrect!"+"\n")
results_txt+="\nAccuracy: " + str(correct_pred_count/total_count)

with open ('prediction.txt', 'w') as file:  
    file.write(results_txt) 
