import pandas as pd

def load_csv(csv_file):
    return pd.read_csv(csv_file)

def print_dataframe(df,print_column=True,print_rows=True):

    if print_column:
        print( ",".join([key for key in df]))
    if print_rows:
        for index, row in df.iterrows():
            print(",".join([str(row[column]) for column in df]))

def find_nan_in_each_column(df:pd.DataFrame):
    for column in df:
        nan = df[column].isnull().sum()
        print(column,nan)
def drop_unwanted_column(df:pd.DataFrame,drop_list):
    '''
    DataFrame.drop(labels=None,axis=0,index=None,columns=None,inplace=False,....)
    labels: 单个标签或者类似list，index或者columns
    axis:   0=index,1=columns
    index和colunms 指定替代方法
    inplace:False返回副本,True原地修改
    '''
    return df.drop(labels=drop_list,axis=1,inplace=False) #等价于df.drop(columns=drop_list)

if __name__ == "__main__":
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]
    csv_file = "Books.csv"
    df = load_csv(csv_file)

    print_dataframe(df,print_rows=False)

    dropped_df = drop_unwanted_column(df,columns_to_drop)

    print_dataframe(dropped_df,print_rows=False)
