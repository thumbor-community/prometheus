# -*- coding: utf-8 -*-
from thumbor.config import Config

Config.define(
        'PROMETHEUS_SCRAPE_PORT',
        8000,
        'Port the prometheus client should listen on',
        'Metrics'
)
