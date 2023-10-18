# Redis Basics Project

In this project, you will learn how to work with Redis for basic operations and utilize Redis as a simple cache.

## Learning Objectives

By the end of this project, you will be able to:

1. **Learn how to use Redis for basic operations**: Gain a fundamental understanding of Redis and its key-value data store for various data manipulation tasks.

2. **Learn how to use Redis as a simple cache**: Explore Redis as a caching mechanism to improve the performance of your applications by efficiently storing and retrieving frequently accessed data.

## Requirements

- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should adhere to the pycodestyle style (version 2.5).
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)`).
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)`).
- All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`).
- The documentation should be descriptive sentences explaining the purpose of the module, class, or method (the length will be verified).
- All your functions and coroutines must be type-annotated.

## Installation and Setup

### Install Redis on Ubuntu 18.04

To install Redis on Ubuntu 18.04, run the following commands:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
