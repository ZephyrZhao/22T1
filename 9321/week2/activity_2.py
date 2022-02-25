import pandas as pd
import sqlite3
from pandas.io import sql

def read_csv(csv_file):
    return pd.read_csv(csv_file)

def write_in_sqlite(dataframe,database_file,table_name):
    """
    :param dataframe: The dataframe which must be written into the database
    :param database_file: where the database is stored
    :param table_name: the name of the table
    """
    # 连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象。
    cnn = sqlite3.connect(database_file)
    # 
    sql.to_sql(frame=dataframe,name=table_name,con = cnn)
    # 提交当前事务，如果微调用，此次修改对于其他数据库connection是不可见的
    cnn.commit()
    # 关闭数据库，不会自动调用commit()
    cnn.close()

def read_from_sqlite(database_file, table_name):
    """
    :param database_file: where the database is stored
    :param table_name: the name of the table
    :return: A Dataframe
    """
    cnn = sqlite3.connect(database=database_file)
    dataframe = sql.read_sql('select * from '+table_name, cnn)
    cnn.close()
    return dataframe

if __name__ == '__main__':
    table_name = "Demographic_Statistics"
    database_file = 'Demographic_Statistics.db'  # name of sqlite db file that will be created
    csv_file = 'Demographic_Statistics_By_Zip_Code.csv'  # path to the downloaded csv file
    loaded_df = read_csv(csv_file)

    print("Creating database")
    write_in_sqlite(loaded_df, database_file, table_name)
    print("Created Successfully")

    print("Querying the database")
    queried_df = read_from_sqlite(database_file, table_name)