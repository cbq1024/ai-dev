from pymongo import MongoClient


def get_collection(dbname, collection_name):
    """
    返回指定数据库中的指定集合
    :param dbname: 数据库名
    :param collection_name: 集合名
    :return: collection
    """
    # 实例化一个mongo客户端, 服务器地址：localhost(本地)，端口号：27017
    client = MongoClient("mongodb://localhost:27017")
    # 获取指定数据库
    database = client[dbname]
    # 获取数据库中的集合
    collection = database[collection_name]
    return collection


def insert():
    """
    插入数据
    """
    try:
        # 连接MongoDB，指定连接数据库名，指定连接表名。
        collection = get_collection("School", "student")  # 数据库名: School 集合名: student
        # 实例化文档
        doc1 = {"sname": "Mary", "sage": 25}
        doc2 = {"sname": "Bob", "sage": 20}
        documents = [doc1, doc2]
        # 插入文档
        collection.insert_many(documents)
        print("插入成功")
    except Exception as e:
        print(f"发生错误: {e}")


def find():
    """
    查询数据
    """
    try:
        collection = get_collection("School", "student")  # 数据库名: School 集合名: student
        # 查询所有数据
        cursor = collection.find()
        for document in cursor:
            print(document)
    except Exception as e:
        print(f"发生错误: {e}")


def update():
    """
    更新数据
    """
    try:
        collection = get_collection("School", "student")  # 数据库名: School 集合名: student
        # 更新文档，将sname='Mary'的文档修改为sage=22
        collection.update_many({"sname": "Mary"}, {"$set": {"sage": 22}})
        print("更新成功")
    except Exception as e:
        print(f"发生错误: {e}")


def delete():
    """
    删除数据
    """
    try:
        collection = get_collection("School", "student")  # 数据库名: School 集合名: student
        # 删除符合条件的第一个文档
        collection.delete_one({"sname": "Bob"})
        # 删除所有符合条件的文档
        # collection.delete_many({"sname": "Bob"})
        print("删除成功")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    # insert()  # 插入数据
    find()  # 查找数据
    update()  # 更新数据
    find()  # 查找数据
    # delete()  # 删除数据
    find()  # 查找数据

