# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
This project adheres to [CHANGELOG](http://keepachangelog.com).

## [4.0.0] - 2025-04-05
### Changed *breaking*
- Renamed `original_image.fetch` metric to `original_image.fetch.count` and
  `original_image.fetch.latency`, as the upstream `thumbor` was renaming them
  accordingly (see thumbor/thumbor#1720). This will change the specific metrics
  with this name having that prefix. ([mkobel](https://github.com/mkobel))

  **Make sure all your alerting rules and dashboards are adjusted accordingly!**

## [3.0.0] - 2024-10-24
### Added
- Multiprocess support to use the [--processes](https://thumbor.readthedocs.io/en/7.4.4/running.html#processes) parameter of thumbor
  by setting the [PROMETHEUS\_MULTIPROC\_DIR](https://prometheus.github.io/client_python/multiprocess/) environment variable.
  ([VladVolchkov](https://github.com/VladVolchkov))
### Changed *breaking*
- Removed `_incr` postfix for `counter` metrics, as the upstream `thumbor` was renaming them
  accordingly (see thumbor/thumbor#1462). This will change all metric names of type `counter`.
  **Make sure all your alerting rules and dashboards are adjusted accordingly!**

## [2.0.0] - 2022-08-19
### Fixed
- Fixed https://github.com/thumbor/thumbor/pull/1462 ([mbarouski](https://github.com/mbarouski))

## [1.0.0] - 2022-07-01
### Changed
- Python 3 and Thumbor 7 support ([mbarouski](https://github.com/mbarouski))
- Removed pyvows in favor of pytest ([mbarouski](https://github.com/mbarouski))

## [0.1.1] - 2017-03-17
### Fixed
- fixed hard coded label mapping not matching with prefix 'thumbor\_'

## [0.1.0] - 2017-02-23
### Added
- initial metrics class
- initial tests
- initial documentation and related files
