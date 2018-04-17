from math import floor
import sys
import pickle
import redis

conn = redis.StrictRedis(host='localhost', port=6379, db=0)

priority_list = ['p1', 'p2'] 

priority1 = { "p1": {"count": 0, "avg": 0, "max": 0, "min": 0}}
priority2 = { "p2": {"count": 0, "avg": 0, "max": 0, "min": 0}}

def set_stats_redis(redis_data, redis_key):
    p_redis_data = pickle.dumps(redis_data)
    conn.set(redis_key, p_redis_data)

def get_stats_redis(redis_key):
    read_redis_key = conn.get(redis_key)
    new_redis_data = pickle.loads(read_redis_key)
    return new_redis_data

for i in range(len(priority_list)):
    print priority_list[i]

def check_data(priority):
    if priority in priority_num:
      response(priority, count_num, p_dic, average)

def response(pdata, count_num, redis_stats, average):
    redis_stats[pdata]['count'] += 1
    # set max if count_num is greater the current max number
    if redis_stats[pdata]['max'] > count_num:
        redis_stats[pdata]['max'] = count_num   
    if redis_stats[pdata]['min'] < count_num:
        redis_stats[pdata]['min'] = count_num  
    average.append(count_num)
    fullcount = len(average)
    averagesum = 0 
    if fullcount > 1:
        for num in average:
            averagesum += num
        new_avg = int(floor(averagesum / fullcount))
        redis_stats[pdata]['avg'] = new_avg
    print averagesum
    print fullcount
    #print new_avg
    print average
    redis_data = redis_stats
    set_stats_redis(redis_data, pdata)
    return redis_stats

def runwithit(priority_list, newdata):
    for i in range(len(priority_list)):
        pdata =  priority_list[i]
        if pdata in newdata:
            count_num = newdata[pdata]
            print "%s %s" % (count_num, pdata)
            #response(pdata, count_num, p_dic, average)

response(pdata, count_num, redis_stats, average)
