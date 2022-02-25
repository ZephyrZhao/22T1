import json
import pandas as pd
from pymongo import MongoClient
import ipdb

def read_csv(csv_file):
    """
    :param csv_file: the path of csv file
    :return: A dataframe out of the csv file
    """
    return pd.read_csv(csv_file)
    


def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))


def write_in_mongodb(dataframe, mongo_host, mongo_port, db_name, collect):
    """
    :param dataframe: 
    :param mongo_host: Mongodb server address 
    :param mongo_port: Mongodb server port number
    :param db_name: The name of the database
    :param collection: the name of the collection inside the database
    """
    # ipdb.set_trace()
    # 创建数据库连接对象
    client = MongoClient()
    # 选择一个数据库
    db = client[db_name]
    # 选择一个集合
    collection = db[collect]
    # You can only store documents in mongodb;
    # so you need to convert rows inside the dataframe into a list of json objects
    # dataframe.T.to_json() 返回一个json字符串 .T是将dataframe进行转置，然后再转成json字符串
    # json.loads() 返回json对象
    records = json.loads(dataframe.T.to_json()).values()
    # 在MongoDB中，每条数据都有一个_id来唯一标识，如果没有显式指明_id，MongoDB会自动产生一个ObjectId类型的_id。
    # insert()方法会在执行后返回的_id值
    # 我们也可以同时插入多条数据，传入A iterable of documents to insert(如列表)
    collection.insert_many(records)


def read_from_mongodb(mongo_host, mongo_port, db_name, collection):
    """
    :param mongo_host: Mongodb server address 
    :param mongo_port: Mongodb server port number
    :param db_name: The name of the database
    :param collection: the name of the collection inside the database
    :return: A dataframe which contains all documents inside the collection
    """
    client = MongoClient(host=mongo_host, port=mongo_port)
    # client['数据库名称'] 返回要使用的数据库
    db = client[db_name]
    # MongoDB的每个数据库又包含了许多集合Collection，也就类似与关系型数据库中的表，我们需要指定要操作的集合
    # e.g. 指定操作学生集合，db['students']
    c = db[collection]
    # 集合.find() 或者 集合.findone() 查询多条或一条结果， 
    # 多条结果返回 Cursor 类型，是一个生成器
    # 每条结果是dic，类似于json
    return pd.DataFrame(list(c.find()))


if __name__ == '__main__':

    db_name = 'comp9321'
    mongo_port = 27017
    mongo_host = 'localhost'

    csv_file = 'Demographic_Statistics_By_Zip_Code.csv'  # path to the downloaded csv file
    df = read_csv(csv_file)
    collect = 'Demographic_Statistics'

    print("Writing into the mongodb")
    write_in_mongodb(df, mongo_host, mongo_port, db_name, collect)

    print("Querying the database")
    df = read_from_mongodb(mongo_host, mongo_port, db_name, collect)

    print_dataframe(df)