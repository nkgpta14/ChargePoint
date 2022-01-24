from helper.count_validation import count_validation
import pandas as pd
from helper.creating_dataframes import df1, df2


def csv_file_comparison():

    global df
    try:
        if count_validation() == 'FAIL':
            df = pd.concat([df1, df2])
            df = df.reset_index(drop=True)
            df_gpby = df.groupby(list(df.columns))
            print(list(df.columns))
            unique_record_idx = [x[0] for x in df_gpby.groups.values() if len(x) >= 1]
            print(unique_record_idx)
            df = df.reindex(unique_record_idx)
        return df
    except Exception as e:
        print(f'csv_file_comparison - {e}')
    #    exit()