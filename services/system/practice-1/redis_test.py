import redis


r = redis.Redis(host="localhost", port=6379, decode_responses=True)

print(r.ping())
print(r.set(name="야", value="호"))
print(r.get(name="야"))