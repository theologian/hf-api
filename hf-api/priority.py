from math import floor
import sys
import pickle
import redis
import json
import ast

conn = redis.StrictRedis(host='localhost', port=6379, db=0)

def run_once():
    p1 = { "p1": {"count": 0, "avg": 0, "max": 0, "min": 0}}
    p2 = { "p2": {"count": 0, "avg": 0, "max": 0, "min": 0}}
    average = [] 
    set_stats_redis(p1, 'p1')
    set_stats_redis(p2, 'p2')
    set_stats_redis(average, 'average')
    pdata = {}
    print "run_once ran"

def set_stats_redis(redis_data, redis_key):
    p_redis_data = pickle.dumps(redis_data)
    conn.set(redis_key, p_redis_data)

def get_stats_redis(redis_key):
    read_redis_key = conn.get(redis_key)
    new_redis_data = pickle.loads(read_redis_key)
    #return new_redis_data

def response(pdata, count_num, redis_stats):
    redis_stats = json.loads(redis_stats)
    print type(redis_stats)
    redis_stats[pdata]['count'] += 1
    # set max if count_num is greater the current max number
    if redis_stats[pdata]['max'] < count_num:
        redis_stats[pdata]['max'] = count_num   
    if redis_stats[pdata]['min'] > count_num:
        redis_stats[pdata]['min'] = count_num  
    average = get_stats_redis('average')
    average.append(count_num)
    fullcount = len(average)
    averagesum = 0 
    if fullcount > 1:
        for num in average:
            averagesum += num
        new_avg = int(floor(averagesum / fullcount))
        redis_stats[pdata]['avg'] = new_avg
        set_stats_redis(average, 'average')
    set_stats_redis(redis_stats, pdata)
    redis_data_json = json.dumps(redis_stats)
    print redis_data_json

def runwithit(newdata):
    priority_list = ['p1', 'p2']
    for i in range(len(priority_list)):
        pdata =  priority_list[i]
        if pdata in newdata:
            print 'good'
            newdata = json.loads(newdata)
            count_num = newdata[pdata]
            redis_stats = get_stats_redis(pdata)
            print "%s %s %s" % (count_num, pdata, newdata)
            response_data = response(pdata, count_num, redis_stats)
            return response_data
