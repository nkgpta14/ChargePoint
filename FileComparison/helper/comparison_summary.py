from helper.count_validation import count_validation
from helper.creating_dataframes import df1
import pandas as pd


def comparison_summary(failed_column_list):

    global status, column_names
    comparison = []
    try:
        for k in range(0, df1.shape[1]):
            if count_validation() == 'PASS':
                if df1.columns[k] in failed_column_list:
                    status = 'FAIL'
                else:
                    status = 'PASS'
                column_names = df1.columns.values[k]
            else:
                status = 'FAIL'
                column_names = df1.columns.values[k]
            comparison.append([column_names, status])
        df = pd.DataFrame(comparison, columns=['Column Names', 'Comparison Status'])
        df_comparison = df[['Column Names', 'Comparison Status']]
        print('Getting comparison_summary for excel is successful')
        return df_comparison
    except Exception as e:
        print(f'comparison_summary - {e}')
        #exit()
