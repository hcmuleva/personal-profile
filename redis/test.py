import redis
r = redis.Redis(host="127.0.0.1", port=6379, db=1)
# res = r.mset({"fname": "Aaditya", "sname": "muleva"})
# print(res)
res = r.get("sname")
print(res)
