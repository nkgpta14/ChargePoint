import pandas as pd
from helper.count_validation import count_validation
from helper.creating_dataframes import df1, df2


def file_count_summary():

    try:
        df_files = pd.DataFrame(
            {'Count Validation': [count_validation()], 'File1': [df1.shape[0]],
             'File2': [df2.shape[0]]})
        df_count = df_files[['Count Validation', 'File1', 'File2']]
        print('File count summary is ready to be printed on excel')
        return df_count
    except Exception as e:
        print(f'file_count_summary - {e}')
        #exit()