import pymongo

client = pymongo.MongoClient("mongodb+srv://tinkuhore:Bolbokeno1994@cluster0.8jywj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    'name': 'Tinku',
    'emain_id': 'tinku.doitnow@gmail.com',
    'surname': 'Hore'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )