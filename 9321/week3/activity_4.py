import pandas as pd


def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))


def clean(dataframe):
    dataframe['Place of Publication'] = dataframe['Place of Publication'].apply(
        lambda x: 'London' if 'London' in x else x.replace('-', ' '))

    new_date = dataframe['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    new_date = pd.to_numeric(new_date)
    new_date = new_date.fillna(0)
    dataframe['Date of Publication'] = new_date

    return dataframe


if __name__ == "__main__":
    csv_file = "Books.csv"
    books_df = pd.read_csv(csv_file)
    books_df = clean(books_df)
    # Replace the spaces with the underline character ('_')
    # Because panda's query method does not work well with column names which contains white spaces
    books_df.columns = [c.replace(' ', '_') for c in books_df.columns]

    city_df = pd.read_csv('City.csv')

    # merge the two dataframes
    '''
    def merge(
    left: DataFrame | Series,             拼接的左侧DataFrame对象
    right: DataFrame | Series,            拼接的右侧DataFrame对象
    how: str = "inner",                   'inner','outer','left','right' 交集，并集，只左采用左df的key，只右采用左df的key，
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,    左侧DataFrame中的列或索引级别用作键
    right_on: IndexLabel | None = None,   右侧DataFrame中的列或索引级别用作键
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    copy: bool = True,
    indicator: bool = False,
    validate: str | None = None,
    )-> DataFrame:
    '''
    df = pd.merge(books_df, city_df, how='left', left_on=['Place_of_Publication'], right_on=['City'])

    # Group by Country and keep the country as a column
    '''
    df.groupby(by,axis=0,as_index=True) 
    函数返回的对象是一系列(key,values)，其中key是分组的字段值，value是该字段值下的table。
    by :接收映射、函数、标签或标签列表；用于确定聚合的组。
    axis : 接收 0/1；用于表示沿行(0)或列(1)分割。
    as_index：接收布尔值，默认Ture；Ture则返回以组标签为索引的对象，False则不以组标签为索引。
    '''
    gb_df = df.groupby(by=['Country'], as_index=False)

    # Select a column (as far as it has values for all rows, you can select any column)
    df = gb_df['Identifier'].count()

    # print the dataframe which shows publication number by country
    print_dataframe(df)
