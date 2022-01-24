import pandas as pd
from library import ConfigReader

file1 = ConfigReader.readConfigData('Details', 'file1')
file2 = ConfigReader.readConfigData('Details', 'file2')

def creating_dataframe(file_name):

    try:
        df = pd.read_csv(file_name, low_memory=False).astype(str)
        return df
    except Exception as e:
        print(f'creating_dataframe - {e}')
        #exit()


df1 = creating_dataframe(file1)
df2 = creating_dataframe(file2)
