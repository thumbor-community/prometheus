# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='tc_prometheus',
    version="0.1.1",
    description='Thumbor Prometheus metrics extension',
    author='Simon Effenberg',
    author_email='savar@schuldeigen.de',
    url='https://github.com/thumbor-community/prometheus',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'thumbor',
        'prometheus_client',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
    long_description="""
Prometheus metrics extension enables thumbor to expose a scrape endpoint prometheus can scrape from.
"""
)
