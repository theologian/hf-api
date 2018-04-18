from math import floor
from werkzeug.datastructures import ImmutableMultiDict
import pickle, redis, logging, pdb

conn = redis.StrictRedis(host='localhost', port=6379, db=0)
priority_log = "/var/log/priority.log"

logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s %(levelname)s %(message)s',
                    filename = priority_log,
                    filemode = 'w')

def run_once():
    p1 = { "p1": {"count": 0, "avg": 0, "max": 0, "min": 99999999999}}
    p2 = { "p2": {"count": 0, "avg": 0, "max": 0, "min": 99999999999}}
#    average = [] 
    set_stats_redis(p1, 'p1')
    set_stats_redis(p2, 'p2')
    set_stats_redis(average, 'p2_average')
    set_stats_redis(average, 'p1_average')
    logging.info("run_once ran")
    print "run_once ran"

def set_stats_redis(redis_data, redis_key):
    p_redis_data = pickle.dumps(redis_data)
    conn.set(redis_key, p_redis_data)
    logging.info("set_stats_redis ran")

def get_stats_redis(redis_key):
    read_redis_key = conn.get(redis_key)
    new_redis_data = pickle.loads(read_redis_key)
    logging.info("get_stats_redis ran : redis_key =  %s" % (redis_key))
    return new_redis_data

def response(pdata, count_num):
    redis_stats = get_stats_redis(pdata)
    redis_stats[pdata]['count'] += 1
    # set max if count_num is greater the current max number
    if redis_stats[pdata]['max'] < count_num:
        redis_stats[pdata]['max'] = count_num   
    if redis_stats[pdata]['min'] > count_num:
        redis_stats[pdata]['min'] = count_num  
    paverage = pdata + '_' +'average'
    average = get_stats_redis(paverage)
    average.append(count_num)
    fullcount = len(average)
    averagesum = 0 
    if fullcount > 1:
        for num in average:
            averagesum += int(num)
        new_avg = int(floor(averagesum / fullcount))
        redis_stats[pdata]['avg'] = new_avg
        logging.info("response ran : new_avg =  %s" % (fullcount))
        set_stats_redis(average, paverage)
    set_stats_redis(redis_stats, pdata)
    logging.info("response ran : set_stats_redis =  %s" % (set_stats_redis))
    return redis_stats

def get_priority(newdata, pdata):
    count_num = int(newdata[pdata])
    new_redis_counts = response(pdata, count_num)
    logging.info("get_priority ran : new_redis_counts =  %s" % (new_redis_counts))
    return new_redis_counts

def run_priority(newdata):
    newdata = newdata.to_dict()
    updated_redis_full = {}
    for key, value in newdata.items():
        pdata =  key
        pdata + 'updated_redis'
        updated_redis = get_priority(newdata, pdata)
        updated_redis_full.update(updated_redis)
        logging.info("run_priority ran : run_priority =  %s" % (run_priority))
    return updated_redis_full
