#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests

# Initialize a Redis connection
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    """ Track how many times a particular URL was accessed in the key
        "count:{url}" and cache the result with an expiration time of 10 seconds """
    count_key = f"count:{url}"
    cache_key = f"cached:{url}"

    # Check if the data is already in the cache
    cached_data = r.get(cache_key)
    if cached_data:
        # Increment the access count
        r.incr(count_key)
        return cached_data.decode('utf-8')

    # If not in cache, fetch the data from the web
    resp = requests.get(url)
    data = resp.text

    # Store the data in the cache with an expiration time
    r.setex(cache_key, 10, data)
    # Increment the access count
    r.incr(count_key)

    return data

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
