from pymongo import MongoClient

# Connect to the MongoDB server using the URI
uri = "mongodb+srv://administrator:IOxGWXj1DBEAzYxw@provacluster.e8xxuwe.mongodb.net/test"
client = MongoClient(uri)

# Choose the database and collection where you want to insert data
db = client["ProvaDataBase"]
collection = db["ProvaCollection"]

# Create a document to insert
document = {
  "field_1": "value_1",
  "field_2": "value_2",
}

# Insert the document into the collection
collection.insert_one(document)

# Close the connection to the MongoDB server
client.close()
