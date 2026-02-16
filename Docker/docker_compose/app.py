import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while retries > 0:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            retries -= 1
            time.sleep(0.5)
    
    raise ConnectionError("Could not connect to Redis after several retries")

@app.route('/')
def hello():
    count = get_hit_count()
    return "<h1>Hello Madhav! I have been seen {} times.\n </h1>".format(count)

if __name__ == "__main__":
    app.run(debug=True)
