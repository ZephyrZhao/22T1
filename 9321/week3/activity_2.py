import pandas as pd
from activity_1 import load_csv

def uniform_data(df:pd.DataFrame):
    # Replace the cell value of "Place of Publication" with "London" if it contains "London",
    # and replace all '-' characters with space
    # We use the apply method which applies a lambda function to the cells of a dataframe
    df['Place of Publication'] = df['Place of Publication'].apply(
        lambda x: 'London' if 'London' in x else x.replace('-', ' '))

def extract_func(df:pd.DataFrame):
    '''
    pandas 分列之.str.extract()
    --  切片 df['Date of Publication'].str[:4]后，
        在data添加一列 df['cut_Date'] = df['Date of Publication'].str[:4]
        像添加字典(key:value)一样，切片出来的不是DataFrame，不需要merge()操作
    --  str.extract() + 正则表达式 处理更为复杂的混合字符串

    '''
    # 此时的new_date是str形式的
    # .str.extract()的结果是DataFrame, expand=False 则返回series
    new_date = df['Date of Publication'].str.extract('^(\d{4})',expand=False)

    new_date = pd.to_numeric(new_date,downcast='integer')
    # df['Date of Publication'] = new_date

    # replace all NaN with 0
    new_date = new_date.fillna(0)

if __name__ == "__main__":
    csv_file = "Books.csv"
    df = pd.read_csv(csv_file)

    uniform_data(df)
    ################################################################################################################
    # Here is also another approach using numpy.where                                                              #
    #    import numpy as np                                                                                        #
    #    london = df['Place of Publication'].str.contains('London')                                                #
    #    df['Place of Publication'] = np.where(london, 'London', df['Place of Publication'].str.replace('-', ' ')) #
    ################################################################################################################
    print(df['Place of Publication'])

    # We use Pandas' extract method which for each subject string in the Series,
    # extracts groups from the first match of regular expression pat.
    print('************************************')
    extract_func(df)

    # new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    # # ^(\d{4}) : matches 4 digit numbers in the beginning of the string
    # new_date = pd.to_numeric(new_date)
    # df['Date of Publication'] = new_date
    # print(df['Date of Publication'])

    # # replace all NaN with 0
    # new_date = new_date.fillna(0)
    # df['Date of Publication'] = new_date
    # print(df['Date of Publication'])
