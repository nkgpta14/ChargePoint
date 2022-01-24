from helper.creating_dataframes import df2, df1


def header_comparison():
    try:
        if (df2.shape[1] - df1.shape[1]) == 0:
            print('Header Validation has been passed successfully')
            pass
        else:
            print(f'''
                    File1 and File2 are not synced
                    File1 has {(df1.shape[1])} columns
                    File2 has {(df2.shape[1])} columns''')
    except Exception as e:
        print(f'columns_validation - {e}')
        exit()