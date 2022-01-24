import numpy as np
import pandas as pd
from helper.convert_to_str import convert_to_str
from helper.creating_dataframes import df1, df2
from helper.csv_comparison import csv_file_comparison
from helper.primary_Keys import primary_keys
from library import ConfigReader


excel_report = ConfigReader.readConfigData('Details', 'Excel_Report')

def detailed_comparison():

    global df_failed_records, file1_value, file2_value, failed_column, pk_column, pk_value

    try:
        failed_records = []
        failed_column_list = []
        failed_column = []

        cnt = 0
        if df1.shape[0] == df2.shape[0]:
            comparison_values = df1.values == df2.values
            np_array = np.array(comparison_values)
            print('np_array - Comparison is done')
            print(np_array)

            for i in range(0, df1.shape[0]):
                for j in range(0, df1.shape[1]):

                    if np_array[i, j] == False:
                        file1_value = df1[df1.columns.values[j]].values[i]
                        file2_value = df2[df2.columns.values[j]].values[i]
                        failed_column = df1.columns.values[j]
                        pk_column_list = primary_keys()
                        pk_column = convert_to_str(pk_column_list, ' | ')
                        pk_value_list = df1[pk_column_list].values[i]
                        pk_value = convert_to_str(pk_value_list, ' | ')

                        failed_records.append([pk_column, pk_value, failed_column, file1_value, file2_value])
                    failed_column_list.append(failed_column)
                cnt += 1
                print(f'{cnt} rows are written')

        else:
            df = pd.DataFrame()
            df = df.append(csv_file_comparison())
            df_merge = df1.merge(df2, how='outer', indicator=True, on=primary_keys())
            merged_with_exist_df = pd.merge(df, df_merge, how='outer', indicator='Exist', on=primary_keys())
            merged_with_exist_df['Exist'] = np.where(merged_with_exist_df.Exist == 'both', True, False)
            unique_nonmatching_df = merged_with_exist_df.loc[merged_with_exist_df['Exist'] == True].iloc[:].drop_duplicates()

            for i in range(len(unique_nonmatching_df)):

                if unique_nonmatching_df['_merge'].values[i] == 'left_only':
                    base_file_value_list = unique_nonmatching_df[primary_keys()].values[i]
                    file2_value = 'Null'
                    file1_value = convert_to_str(base_file_value_list, ' | ')
                    failed_column = convert_to_str(primary_keys(), ' | ')
                    pk_column = failed_column
                    pk_value = file1_value
                    failed_records.append([pk_column, pk_value, failed_column, file1_value, file2_value])

                elif unique_nonmatching_df['_merge'].values[i] == 'right_only':
                    file1_value = 'Null'
                    test_file_value_list = unique_nonmatching_df[primary_keys()].values[i]
                    file2_value = convert_to_str(test_file_value_list, ' | ')
                    failed_column = convert_to_str(primary_keys(), ' | ')
                    pk_column = failed_column
                    pk_value = file2_value
                    failed_records.append([pk_column, pk_value, failed_column, file1_value, file2_value])

                elif unique_nonmatching_df['_merge'].values[i] == 'both':
                    records_in_both_df = unique_nonmatching_df[primary_keys()[0]].values[i]
                    df1_length_common_records = len(df1[primary_keys()][df1[primary_keys()[0]] == records_in_both_df])
                    df2_length_common_records = len(df2[primary_keys()][df2[primary_keys()[0]] == records_in_both_df])
                    loop = 0

                    if df1_length_common_records > df2_length_common_records:
                        itr_times = df1_length_common_records - df2_length_common_records
                        while loop < itr_times:
                            base_file_value_list = unique_nonmatching_df[primary_keys()].values[i]
                            file2_value = 'Null'
                            file1_value = convert_to_str(base_file_value_list, ' | ')
                            failed_column = convert_to_str(primary_keys(), ' | ')
                            pk_column = failed_column
                            pk_value = file1_value
                            failed_records.append([pk_column, pk_value, failed_column, file1_value, file2_value])
                            loop += 1

                    elif df1_length_common_records < df2_length_common_records:
                        itr_times = df2_length_common_records - df1_length_common_records
                        while loop < itr_times:
                            file1_value = 'Null'
                            test_file_value_list = unique_nonmatching_df[primary_keys()].values[i]
                            file2_value = convert_to_str(test_file_value_list, ' | ')
                            failed_column = convert_to_str(primary_keys(), ' | ')
                            pk_column = failed_column
                            pk_value = file2_value

                            failed_records.append([pk_column, pk_value, failed_column, file1_value, file2_value])
                            loop += 1
                failed_column_list.append(failed_column)
                cnt += 1
                print(f'{cnt} rows are written')
        df_failed_records = pd.DataFrame(failed_records,
            columns=['Primary Key Column', 'Primary Key value', 'Failed Column', 'File1 Value', 'File2 Value'])
        print('Detailed Comparison is done successfully.')
        print(f'failed_column_list is - {failed_column_list}')
        return failed_column_list
    except Exception as e:
        print(f'detailed_records - {e}')
        #exit()


def merging_dataframes(df_count, df_comparison):

    try:
        dataframes = [df_count, df_comparison]
        merged_df = pd.concat(dataframes, axis=1)

        with pd.ExcelWriter(excel_report) as writer:
            merged_df.to_excel(writer, engine='openpyxl', index=False, header=True, sheet_name='Summary', startrow=5, startcol=5)
            df_failed_records.to_excel(writer, engine='openpyxl', index=False, header=True, sheet_name='Details', startrow=5, startcol=5)
    except Exception as e:
        print(f'merging_dataframes - {e}')
        exit()
