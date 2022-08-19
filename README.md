# Thumbor Prometheus Metrics Plugin [![Build Status](https://travis-ci.org/thumbor-community/prometheus.svg?branch=master)](https://travis-ci.org/thumbor-community/prometheus)

Collecting Thumbor runtime metrics using the prometheus_client and exposes them
via an HTTP endpoint on a configurable port.

## Installation

```bash
# latest stable
pip install tc_prometheus

# master branch
pip install -e git+https://github.com/thumbor-community/prometheus.git@master#egg=tc_prometheus
```

## Configuration

```python
# thumbor.conf
METRICS = 'tc_prometheus.metrics.prometheus_metrics'

# optional with defaults
PROMETHEUS_SCRAPE_PORT = 8000 # Port the prometheus client should listen on
```

## Upgrade notes

### from 1.x to 2.x
The switch from 1.x to 2.x is not requiring any change within thumbors configuration or the plugin itself.
The crucial difference is, that some metrics will be renamed, so that you might need to update your monitoring/alarming.
Also be aware that you will get a lot more metrics until the old ones cease to exit which can be okay but on big
installation it might create issues by itself.
