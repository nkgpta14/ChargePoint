from helper.header_comparison import header_comparison
from helper.comparison_summary import comparison_summary
from helper.count_validation import count_validation
from helper.detailed_comparison import detailed_comparison, merging_dataframes
from helper.file_count_summary import file_count_summary
from reports.reports import excel_formatting


def main1():

    header_comparison()
    count_validation()
    merging_dataframes(file_count_summary(), comparison_summary(detailed_comparison()))
    excel_formatting()



if __name__ == '__main__':
    main1()
