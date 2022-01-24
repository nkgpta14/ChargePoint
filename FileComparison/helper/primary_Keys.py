import ntpath
from data import Data
from library import ConfigReader


def get_file_name(path):
    head, tail = ntpath.split(path)
    return tail


def primary_keys():
    try:
        workbook = Data.getWorkBook(ConfigReader.readConfigData('Details', 'Primary_Key'))
        primary_key = []

        worksheet = workbook.active
        rows = Data.getRowCount(worksheet)
        columns = Data.getColumnCount(worksheet)
        for row_num in range(2, rows + 1):
            c = Data.readcell(worksheet, row_num, 1)
            if c.value in get_file_name(ConfigReader.readConfigData('Details', 'file1')):
                for col_num in range(2, columns + 1):
                    if Data.readcell(worksheet, row_num, col_num).value is not None:
                        primary_key.append(Data.readcell(worksheet, row_num, col_num).value)
        #print(f'Primary Keys are {primary_key}')
        return primary_key
    except Exception as e:
        print(f'sort_keys - {e}')
    #    exit()
