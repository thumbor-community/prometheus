# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='tc_prometheus',
    version="0.1.0",
    description='Thumbor Prometheus metrics extension',
    author='Simon Effenberg',
    author_email='savar@schuldeigen.de',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'thumbor',
        'prometheus_client',
    ]
)
