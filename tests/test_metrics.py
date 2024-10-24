#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2022 Thumbor Community Extensions

from unittest import TestCase
from preggy import expect
import pytest

from thumbor.context import Context
from thumbor.importer import Importer
from thumbor.config import Config
import thumbor.metrics
import tc_prometheus.metrics.prometheus_metrics

from tornado.httpclient import HTTPClient

class MetricsContext(TestCase):
    def setUp(self):
        self.config = Config()
        self.config.METRICS = 'tc_prometheus.metrics.prometheus_metrics'
        self.config.PROMETHEUS_SCRAPE_PORT = '8001'
        
        self.importer = Importer(self.config)
        self.importer.import_modules()
        
        self.context = Context(None, self.config, self.importer)

    def tearDown(self):
        pass


class CanCreateContextWithPrometheusMetrics(MetricsContext):
    def test_should_be_instance_of_prometheus_metrics(self):
        expect(self.context.metrics).to_be_instance_of(tc_prometheus.metrics.prometheus_metrics.Metrics)

    def test_should_not_fail_on_use(self):
        expect(self.context.metrics.incr('test.count')).Not.to_be_an_error()
        expect(self.context.metrics.incr('test.count', 2)).Not.to_be_an_error()
        expect(self.context.metrics.timing('test.time', 100)).Not.to_be_an_error()

    def test_should_fail_on_use_of_identical_names_for_incr_and_timing_metrics(self):
        expect(self.context.metrics.incr('test')).Not.to_be_an_error()

        with pytest.raises(ValueError):
            # for some unknown reason, `preggy` seems to not catch the exception
            # even though the documentation says so and therefore the wrapper with
            # `pytest.raises` is being used
            expect(self.context.metrics.timing('test', 100)).to_be_an_error()


class PrometheusEndpoint(MetricsContext):
    def setUp(self):
        super().setUp()
        self.http_client = HTTPClient()
        
    def tearDown(self):
        super().tearDown()
        self.http_client.close()
    
    def test_should_present_metrics(self):
        self.context.metrics.incr('test.counter')
        self.context.metrics.incr('test.counter', 5)
        self.context.metrics.timing('test.timer', 150)
        self.context.metrics.timing('test.timer', 350)
        self.context.metrics.incr('response.status.200', 1)
        # without networklocation label
        self.context.metrics.incr("original_image.status.created")
        # with networklocation label
        self.context.metrics.incr("original_image.status.created.images.com")

        response = self.http_client.fetch('http://localhost:8001')

        expect(response.body).Not.to_be_null()

        body = str(response.body)

        expect(body).to_include('thumbor_test_counter_total 6')
        expect(body).to_include('thumbor_test_timer_count 2')
        expect(body).to_include('thumbor_test_timer_sum 500')
        expect(body).to_include('thumbor_response_status_total{statuscode="200"} 1')
