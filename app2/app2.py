import time
import redis
from flask import request, Flask, render_template, session
from flask_session import Session
from flask_mysqldb import MySQL
import json

app2 = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

SESSION_TYPE = 'redis'
SESSION_REDIS = cache
app2.config.from_object(__name__)
Session(app2)

app2.config['MYSQL_HOST'] = 'mysql'
app2.config['MYSQL_USER'] = 'root'
app2.config['MYSQL_PASSWORD'] = 'root'
app2.config['MYSQL_DB'] = 'demo'

mysql = MySQL(app2)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app2.route('/')
def hello_world():
    count = get_hit_count()
    return render_template('index.html', count=count)

@app2.route('/people')
def people():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT firstname, lastname FROM people''')
    results = cursor.fetchall()
    return str(results)

@app2.route('/set/<name>')
def set(name):
    session['name'] = name
    return 'ok'

@app2.route('/get/')
def get():
    count = get_hit_count()
    name = session.get('name', 'not set')
    return render_template('session.html', count=count, name=name)

if __name__ == '__main__':
   app2.run(debug=True, host='0.0.0.0')
