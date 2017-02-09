import mmh3
import redis

BIT_SIZE = 5000000
SEEDS = [x for x in range(50, 57)]

def get_redis(host='localhost', port=6379, db=0):
    return redis.Redis(host='localhost', port=port, db=db)

class BloomFilter(object):

    def __init__(self, key='bloomfilter'):
        self.db = get_redis()
        self.key = key

    def cal_offsets(self, content):
        return [mmh3.hash(content, seed) % BIT_SIZE for seed in SEEDS]

    def is_contains(self, content):
        if not content:
            return False
        locs = self.cal_offsets(content)

        return all(True if self.db.getbit(self.key, loc) else False for loc in locs)

    def insert(self, content):
        locs = self.cal_offsets(content)

        pipe = self.db.pipeline()
        for loc in locs:
            pipe.setbit(self.key, loc, 1)
        pipe.execute()


if __name__ == '__main__':
    bloom_filter = BloomFilter()

    test_url = 'http://www.baidu.com'

    bloom_filter.insert(test_url)

    if bloom_filter.is_contains(test_url):
        print 'OK'
    else:
        print 'False'