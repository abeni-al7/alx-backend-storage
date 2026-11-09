# ALX Backend Storage

Data-storage exercises from the ALX Africa Software Engineering programme (2023–2024), covering advanced SQL, NoSQL, and Redis.

## Contents

| Directory | Topic |
|-----------|-------|
| `0x00-MySQL_Advanced` | SQL scripts: indexes, triggers, stored procedures, functions, views, and ranking queries |
| `0x01-NoSQL` | MongoDB shell commands and PyMongo scripts (CRUD, aggregation, Nginx log stats) |
| `0x02-redis_basic` | A Redis-backed cache class, call counting/history decorators, and an expiring web cache |

## Built with

- MySQL
- MongoDB with PyMongo
- Redis with `redis-py` and `requests`
- Python 3

## Run it

```bash
# SQL
cat 0x00-MySQL_Advanced/4-store.sql | mysql -uroot -p <database>

# MongoDB
cat 0x01-NoSQL/2-insert | mongo my_db
python3 0x01-NoSQL/8-all.py

# Redis
python3 0x02-redis_basic/main.py
```

Educational coursework; each task directory has its own README describing the requirements.
