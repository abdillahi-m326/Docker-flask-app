from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (assumes Redis is running locally on port 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return 'Welcome to the Flask + Redis app!'

@app.route('/count')
def count():
    # Increment the visit count
    count = r.incr('visit_count')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(debug=True)