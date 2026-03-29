#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
print("Connected successfully")
client.close()
