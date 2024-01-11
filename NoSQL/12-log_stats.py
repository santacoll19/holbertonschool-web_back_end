#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

# Create a MongoClient to the running mongod instance
client = MongoClient('mongodb://localhost:27017/')

# Select the 'logs' database and 'nginx' collection
db = client.logs
collection = db.nginx

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents(
    {'method': method}) for method in methods}

# Count the number of logs where method is GET and path is /status
status_count = collection.count_documents({'method': 'GET', 'path': '/status'})

# Display the statistics
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
print(f"{status_count} status check")
