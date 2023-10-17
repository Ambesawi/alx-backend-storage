#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stat() -> None:
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    stats = ""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    stats += "{} logs\nMethods:\n".format(nginx_collection.count_documents({}))
    for m in method:
        method_count = nginx_collection.count_documents({"method": m})
        stats += '\tmethod {}: {}\n'.format(m, method_count)
    stats += "{} status check".format(
        nginx_collection.count_documents({"path": "/status"}))
    stats += '\nIPs:\n'
    top_ips = nginx_collection.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}, {'$limit': 10}])
    for ip in top_ips:
        stats += '\t{}: {}\n'.format(ip.get('_id'), ip.get('count'))
    print(stats, end='')


if __name__ == '__main__':
    log_stat()
