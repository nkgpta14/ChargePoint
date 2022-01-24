from helper.data_cleaning import *

df = [df1, df2]
null_delete_flag = False

def main2(df):

    cnt =1
    for dataframes in df:
        if datacheck(dataframes):
            continue
        else:
            if dataQualityCheck(dataframes):
                data_cleaning(dataframes, cnt)

        # If Null needs to be removed and new file needs to be created
        if null_delete_flag:
            removingNullRecords(dataframes, cnt)
        cnt += 1
    print('Exiting..')


if __name__ == '__main__':
    main2(df)
