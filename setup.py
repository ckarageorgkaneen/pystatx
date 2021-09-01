import io
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.version_info < (3, 0):
    long_description_open = io.open
else:
    long_description_open = open

with long_description_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pystatx',
    version='0.1',
    description='statx(2) wrapper',
    url='https://github.com/ckarageorgkaneen/pystatx',
    packages=['statx'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Tracker': 'https://github.com/ckarageorgkaneen/pystatx/issues',
        'Source': 'https://github.com/ckarageorgkaneen/pystatx',
    },
    license='GPLv3',
    python_requires='>=2.7',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries",
    ]
)
