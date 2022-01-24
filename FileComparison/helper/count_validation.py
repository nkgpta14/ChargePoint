from helper.creating_dataframes import df1, df2


def count_validation():

    try:
        if (df1.shape[0] - df2.shape[0]) == 0:
            print('Count validation has been passed successfully')
            return 'PASS'
        else:
            print(f'File1 has {df1.shape[0]} records')
            print(f'File2 has {df2.shape[0]} records')
            return 'FAIL'
    except Exception as e:
        print(f'count_validation - {e}')
        #exit()