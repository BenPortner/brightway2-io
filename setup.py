from setuptools import setup
import os

setup(
    name='bw2io',
    version="1.0",
    packages=[
        'bw2io',
        'bw2io.export',
        'bw2io.extractors',
        'bw2io.strategies'
        'bw2io.tests',
    ],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE.txt').read(),
    install_requires=[
        "bw2calc",
        "bw2data",
        "lxml",
        "numpy",
        "progressbar-ipython",
        "scipy",
        "stats_arrays",
        "unicodecsv",
        "unidecode",
        "voluptuous",
        "xlsxwriter",
    ],
    url="https://bitbucket.org/cmutel/brightway2-io",
    long_description=open('README.rst').read(),
    description=('Tools for importing and export life cycle inventory databases'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],)
