import pandas as pd
import redis

pool = redis.ConnectionPool(host='10.33.43.204', port=6388, db=1)
r = redis.Redis(connection_pool=pool)

key_list = []
r.pipeline()
keys = r.keys()
for key in keys:
    t = str(key, encoding='utf-8')
    if "哪个医院" in t:
        continue
    t = t.strip("mc-one-qa:")
    key_list.append(t)

pd.DataFrame(key_list).to_csv("key_list.csv", index=False)
