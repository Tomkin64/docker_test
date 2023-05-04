# Docker test

This repo is for test docker skills.

## Docker compose prepare:

- Prometheus
- Grafana - datasource and dashboard
- Alermanager
- Python-app - simple python web service config metrics for Prometheus

## Notes
In folder python-app is my attempt to create python flask app with metrics for Prometheus using prometheus-flask-exporter, but it not working. For testing purpose I found docker image philwinder/prometheus-python which is used instead of my python-app 
