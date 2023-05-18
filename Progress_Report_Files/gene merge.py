import pandas as pd

df = pd.DataFrame()
df_AKT1 = pd.read_csv("AKT1.txt", index_col=1, sep="\t")
df['AKT1']=df_AKT1.iloc[:,[4]]

df_APC = pd.read_csv("APC.txt", index_col=1, sep="\t")
df['APC']=df_APC.iloc[:,[4]]

df_BRAF = pd.read_csv("BRAF.txt", index_col=1, sep="\t")
df['BRAF']=df_BRAF.iloc[:,[4]]

df_CDKN2A = pd.read_csv("CDKN2A.txt", index_col=1, sep="\t")
df['CDKN2A']=df_CDKN2A.iloc[:,[4]]

df_CTNNB1 = pd.read_csv("CTNNB1.txt", index_col=1, sep="\t")
df['CTNNB1']=df_CTNNB1.iloc[:,[4]]

df_EGFR = pd.read_csv("EGFR.txt", index_col=1, sep="\t")
df['EGFR']=df_EGFR.iloc[:,[4]]

df_ERBB2 = pd.read_csv("ERBB2.txt", index_col=1, sep="\t")
df['ERBB2']=df_ERBB2.iloc[:,[4]]

df_FBXW7 = pd.read_csv("FBXW7.txt", index_col=1, sep="\t")
df['FBXW7']=df_FBXW7.iloc[:,[4]]

df_KRAS = pd.read_csv("KRAS.txt", index_col=1, sep="\t")
df['KRAS']=df_KRAS.iloc[:,[4]]

df_MSH2 = pd.read_csv("MSH2.txt", index_col=1, sep="\t")
df['MSH2']=df_MSH2.iloc[:,[4]]

df_MSH6 = pd.read_csv("MSH6.txt", index_col=1, sep="\t")
df['MSH6']=df_MSH6.iloc[:,[4]]

df_NRAS = pd.read_csv("NRAS.txt", index_col=1, sep="\t")
df['NRAS']=df_NRAS.iloc[:,[4]]

df_PIK3CA = pd.read_csv("PIK3CA.txt", index_col=1, sep="\t")
df['PIK3CA']=df_PIK3CA.iloc[:,[4]]

df_PTEN = pd.read_csv("PTEN.txt", index_col=1, sep="\t")
df['PTEN']=df_PTEN.iloc[:,[4]]

df_SMAD4 = pd.read_csv("SMAD4.txt", index_col=1, sep="\t")
df['SMAD4']=df_SMAD4.iloc[:,[4]]

df_SMARCB1 = pd.read_csv("SMARCB1.txt", index_col=1, sep="\t")
df['SMARCB1']=df_SMARCB1.iloc[:,[4]]

df_STK11 = pd.read_csv("STK11.txt", index_col=1, sep="\t")
df['STK11']=df_STK11.iloc[:,[4]]

df_TP53 = pd.read_csv("TP53.txt", index_col=1, sep="\t")
df['TP53']=df_TP53.iloc[:,[4]]

df.to_csv('dataframe.csv')



