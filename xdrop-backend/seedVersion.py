from handlers.db import DBHandler


client = DBHandler.getDBClient()
collection = client['app']

query = {
    '_id': 1
}

data = {
    '$set': {
        'version': '1.0.1'
    }
}

if collection:
    insert = collection.update_one(query, data)
    if insert:
        retrieve = collection.find({})
        for row in retrieve:
            print(row)