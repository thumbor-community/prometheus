#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2017 Simon Effenberg <savar@schuldeigen.de>
# Copyright (c) 2017 Thumbor Community Extensions

import tornado
from tornado_pyvows import TornadoHTTPContext
from pyvows import Vows, expect

from thumbor.context import Context
from thumbor.importer import Importer
from thumbor.config import Config
import thumbor.metrics
import tc_prometheus.metrics.prometheus_metrics


@Vows.batch
class MetricsVows(TornadoHTTPContext):

    def get_app(self):
        application = tornado.web.Application([
            (r"/", None),
            ])
        return application

    class CanCreateContextWithPrometheusMetrics(Vows.Context):
        def topic(self):
            conf = Config()
            conf.METRICS = 'tc_prometheus.metrics.prometheus_metrics'
            imp = Importer(conf)
            imp.import_modules()
            return Context(None, conf, imp)

        def should_initialize_metrics(self, topic):
            expect(topic.metrics).to_be_instance_of(tc_prometheus.metrics.prometheus_metrics.Metrics)

        def should_not_fail_on_use(self, topic):
            expect(topic.metrics.incr('test.count')).not_to_be_an_error()
            expect(topic.metrics.incr('test.count', 2)).not_to_be_an_error()
            expect(topic.metrics.timing('test.time', 100)).not_to_be_an_error()

    class PrometheusEndpoint(TornadoHTTPContext):
        def topic(self):
            conf = Config()
            conf.METRICS = 'tc_prometheus.metrics.prometheus_metrics'
            imp = Importer(conf)
            imp.import_modules()
            return Context(None, conf, imp)

        def should_present_metrics(self, topic):
            topic.metrics.incr('test.counter')
            topic.metrics.incr('test.counter', 5)
            topic.metrics.timing('test.timer', 150)
            topic.metrics.timing('test.timer', 350)
            topic.metrics.incr('response.status.200', 1)

            self.http_client.fetch('http://localhost:8000', self.stop)
            response = self.wait()
            expect(response.body).Not.to_be_null()
            expect(response.body).to_include('thumbor_test_counter 6')
            expect(response.body).to_include('thumbor_test_timer_count 2')
            expect(response.body).to_include('thumbor_test_timer_sum 500')
            expect(response.body).to_include('thumbor_response_status{statuscode="200"} 1')
