# Thumbor Prometheus Metrics Plugin [![Build Status](https://travis-ci.org/thumbor-community/prometheus.svg?branch=master)](https://travis-ci.org/thumbor-community/prometheus)

Collecting Thumbor runtime metrics using the prometheus\_client and exposes them
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

## Multiprocess support

In case thumbor is to be started with multiple processes using the `--processes` argument, the prometheus
client can handle that by the administrator setting the environment variable `PROMETHEUS_MULTIPROC_DIR`.
Please read the corresponding [documentation](https://prometheus.github.io/client_python/multiprocess/) to
understand the implications of that.

Basic example:

```sh
set -e
export PROMETHEUS_MULTIPROC_DIR=/tmp/thumbor/proc_dir
mkdir -p "$PROMETHEUS_MULTIPROC_DIR"
rm -rf "$PROMETHEUS_MULTIPROC_DIR"/* # this is crucial on the 2nd and following runs, but check the documentation
thumbor --processes `nproc` -c /path/to/thumbor.conf
```

## Upgrade notes

### from 2.x to 3.x
All metrics of type `counter` have had before an enforced postfix of `_incr` which is now gone. Therefore
all metrics of type `counter` are renamed and will not match with previously recorded metrics anymore.

**Please make sure to adjust all recording rules, alerting rules and dashboards which are relying on these counters.**

### from 1.x to 2.x
The switch from 1.x to 2.x is not requiring any change within thumbors configuration or the plugin itself.
The crucial difference is, that some metrics will be renamed, so that you might need to update your monitoring/alarming.
Also be aware that you will get a lot more metrics until the old ones cease to exit which can be okay but on big
installation it might create issues by itself.
