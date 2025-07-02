from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using service name as hostname (Docker Compose)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def home():
    return 'Welcome to the Flask + Redis app!'

@app.route('/count')
def count():
    count = r.incr('visit_count')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
