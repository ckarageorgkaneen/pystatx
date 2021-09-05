[![PyPI version](https://badge.fury.io/py/pystatx.svg)](https://badge.fury.io/py/pystatx)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# pystatx: [statx(2)](http://man7.org/linux/man-pages/man2/statx.2.html) python wrapper

statx - get file status (extended)

#### Usage:
e.g. get birth/creation timestamp of file
```python
>>> import statx
>>> statx.statx('some/file').btime
1577040283.7037938
```
