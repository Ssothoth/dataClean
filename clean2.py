import pandas as pd


def read(file):
    return pd.read_csv(file)


def doubleCheck(df, column):
    mask = df.loc[df[column].duplicated(keep=False), :]
    df.loc[mask, column] = ""
    return df


def toNumeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def nullToMean(df, column):
    df.loc[df[column].isnull(), column] = df[column].mean()
    return df


def defaultDateTime(df, column):
    df[column] = pd.to_datetime(df[column], format='%d/%m/%Y', errors='coerce')
    return df

def doubleCorr(df, column):
    mask = df.loc[df[column].duplicated(keep=False), :]
    df.loc[mask, column] = ""
    return df


def corrHeight(df, column):
    df[column] = df[column].str[:-1]
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def corrMails(df, column):
    df[column] = df[column].str.split(',', n=1, expand=True)[0]
    return df
    

def create(df, name):
    df.to_csv(name, index=False)
    return df
