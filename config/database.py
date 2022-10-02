from pymongo import MongoClient

client = MongoClient("mongodb+srv://Rajitha:Rajitha1#$@cluster0.hjtktab.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name=db["todos_app"]

