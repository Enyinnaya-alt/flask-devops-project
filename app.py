# app.py
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Custom metric example
metrics.info('app_info', 'Application info', version='1.0')

@app.route('/')
def hello():
    return "Hello DevOps!"

@app.route('/health')
@metrics.do_not_track()
def health():
    return "OK", 200