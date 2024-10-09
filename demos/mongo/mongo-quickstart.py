import pymongo


def main():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    dev = client["dev"]
    mcdd_collection = dev.collection_mcdd
    for item in mcdd_collection.find().limit(2):
        print(item)

    print([item for item in mcdd_collection.find().sort("_id", pymongo.DESCENDING).limit(3).skip(1)])


if __name__ == '__main__':
    main()
