import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
instance = redis.Redis(connection_pool=pool, protocol=3)
# instance.set('foo', 'bar')
# print(instance.get('foo'))
pipe = instance.pipeline()
pipe.set('foo', 5)
pipe.set('bar', 18.5)
pipe.set('blee', "hello world!")
print(pipe.execute())

pub = instance.pubsub()
pub.subscribe(pipe)
print(pub.get_message())
