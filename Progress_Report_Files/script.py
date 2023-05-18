import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("dataframe.csv", index_col=0)

""" #checking for STD which I was concerned for when looking at the data
df.describe().to_csv('featureProperties.csv') """

# Check whether null values are present
#print(df.isnull().sum())

target_cols = ['AKT1','APC','BRAF','CDKN2A','CTNNB1','EGFR','ERBB2','FBXW7','KRAS','MSH2','MSH6','NRAS','PIK3CA','SMAD4','SMARCB1','STK11','TP53']
feature_cols = ['PTEN']

df_feature = df.loc[:, feature_cols]
df_target = df.loc[:, target_cols]

#Train-Test Spliting
df_feature_train, df_feature_test, df_target_train, df_target_test = train_test_split(df_feature, df_target)

ml_model = LinearRegression()
ml_model.fit(df_feature_train, df_target_train)


# Calculate the model's predictions for our targets
df_target_pred = ml_model.predict(df_feature_test)

# Balanced accuracy for a rough estimate of overall performance
print(f"Balanced Accuracy: {mean_squared_error(df_target_test, df_target_pred)}")