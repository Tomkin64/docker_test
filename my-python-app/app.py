# url: https://docs.docker.com/compose/gettingstarted/
# url2: https://pypi.org/project/prometheus-flask-exporter/
import time

import redis
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
cache = redis.Redis(host='redis', port=6379)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

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

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)

@app.route('/metrics')
def simple_get():
    pass
    
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)