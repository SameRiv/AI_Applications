import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

""" df = pd.read_csv('diabetes_sparse.csv', index_col = 0) """
""" print(np.sum(df.isnull().sum(axis=1)>0)) """
""" print((df.isnull().sum()).sort_values) """

df_diab = pd.read_csv('diabetes_classification.csv', index_col = 0)

diab_features = df_diab.iloc[:, 0:8]
diab_target = df_diab.iloc[:, 8]

""" selector = VarianceThreshold(threshold=0.2)
selector.fit(diab_features)
selected_diab_features = selector.transform(diab_features)

# Rebuild a DataFrame from the results
feature_names = selector.get_feature_names_out()
selected_diab_features = pd.DataFrame(data=selected_diab_features, columns=feature_names)
print(selected_diab_features.columns) """

pca = PCA(n_components=8)
pca_diab_features = pca.fit_transform(diab_features)
col_names = []
for i in range(8):
    col_names.append(f"pc{i}")

pca_diab_features = pd.DataFrame(data=pca_diab_features, columns=col_names)
arriay=(pca.explained_variance_ratio_)
print(arriay)
print(sum(arriay[:5]))
