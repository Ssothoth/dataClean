import pandas as pd

data = pd.read_csv('operations.csv')

print(data.isnull().sum())
nb_na = data.isnull().sum()
print(nb_na[nb_na>0])
print(data.loc[data['montant'].isnull(),:])
data_na = data.loc[data['montant'].isnull(),:]

for index in data_na.index:

    data.loc[data['libelle'] == 'PRELEVEMENT XX TELEPHON XX XX', :]
    data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']
    data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)
data.to_csv('operations.csv', index = False)
