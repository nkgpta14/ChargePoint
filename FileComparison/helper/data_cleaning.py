import pandas as pd
from helper.primary_Keys import *


file1 = ConfigReader.readConfigData('Details', 'file1')
file2 = ConfigReader.readConfigData('Details', 'file2')

df1 = pd.read_csv(file1, low_memory=False)
df2 = pd.read_csv(file2, low_memory=False)


def datacheck(df):
    if df.empty:
        print('Empty dataset')
    return True


def dataQualityCheck(df):
    global missing_values

    missing_values = False
    df = df.isna()

    for i in range(0, df.shape[0]):
        for j in range(0, df.shape[1]):
            if df.loc[i][j]:
                missing_values = True
                break
    if missing_values:
        print('Data Quality Check has been failed')
    else:
        print('Data Quality Check has been passed')
    return missing_values


def data_cleaning(df, cnt):

    df.fillna(value='Null', inplace=True)
    df.to_csv(f'.\\datasets\\file_null'+f'_{cnt}'+'.csv', index=False)
    print(f'file_null' + f'_{cnt}'+'.csv has been generated successfully')
    return df


def removingNullRecords(df, cnt):
    missing_rows = []
    for i in range(0, df.shape[0]):
        for j in range(0, df.shape[1]):
            if df.loc[i][j] == 'Null':
                missing_rows.append(i)
                break

    df.drop(missing_rows, inplace=True)
    df.to_csv(f'.\\datasets\\file_notnull' + f'_{cnt}'+'.csv', index=False)
    print(f'file_notnull' + f'_{cnt}'+'.csv has been generated successfully')
    return df

