# MySQL Project

This project involves working with MySQL and covers various topics related to database management. It aims to enhance your understanding of creating tables with constraints, optimizing queries, and implementing advanced features in MySQL.

## Learning Objectives

By the end of this project, you should be able to:

1. Create tables with constraints in MySQL.
2. Optimize SQL queries by adding indexes for improved performance.
3. Implement and use stored procedures and functions to perform specific tasks within the database.
4. Create and work with views to simplify complex queries and improve data accessibility.
5. Implement triggers to automate actions based on events in the database.

## Project Requirements

**General:**

- Operating System: Ubuntu 18.04 LTS
- MySQL Version: 5.7.30
- All SQL files should have a comment just before the SQL syntax.
- Use uppercase for all SQL keywords (e.g., SELECT, WHERE).
- Start each file with a comment describing the task.
- A README.md file at the root of the project directory is mandatory.

**Using MySQL:**

- Use a container-on-demand to run MySQL.
- Use credentials root/root within the container.
- Start MySQL before working with it.

**Importing SQL Data:**

- Create databases using the CREATE DATABASE command.
- Import SQL dumps using the `mysql` command.

## Usage

To work on the project, follow these general steps:

1. Set up an Ubuntu 18.04 environment with MySQL 5.7.30.
2. Use the provided credentials to access MySQL within the container.
3. Create databases, import SQL data, and implement various MySQL features according to the project requirements.

## Examples

Here is an example of creating a database and importing SQL data:

```bash
$ echo "CREATE DATABASE my_database;" | mysql -uroot -p
Enter password:

$ curl "https://example.com/my_database_dump.sql" -s | mysql -uroot -p my_database
Enter password:

$ echo "SELECT * FROM my_table" | mysql -uroot -p my_database
Enter password:

