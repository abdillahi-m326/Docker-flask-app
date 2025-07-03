from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis connection details from environment variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_db = int(os.environ.get('REDIS_DB', 0))

r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

@app.route('/')
def home():
    return 'Welcome to the Flask + Redis app!'

@app.route('/count')
def count():
    count = r.incr('visit_count')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
