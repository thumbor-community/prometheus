# coding: utf-8

from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'thumbor==7.*,>=7.0.6',
    'prometheus_client==0.*,>=0.14.1',
]

setup(
    name='tc_prometheus',
    version="2.0.0",
    description='Thumbor Prometheus metrics extension',
    author='Simon Effenberg',
    author_email='savar@schuldeigen.de',
    url='https://github.com/thumbor-community/prometheus',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "all": INSTALL_REQUIRES,
        "tests": INSTALL_REQUIRES + [
            'preggy==1.*,>=1.4.4',
            'pytest==8.*,>=8.0.0',
            'pytest-cov==5.*,>=5.0.0',
        ],
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    long_description="""
Prometheus metrics extension enables thumbor to expose a scrape endpoint prometheus can scrape from.
"""
)
