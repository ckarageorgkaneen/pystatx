# pystatx: [statx(2)](http://man7.org/linux/man-pages/man2/statx.2.html) python wrapper

statx - get file status (extended)

#### Usage:
e.g. get birth/creation timestamp of file
```python
>>> import statx
>>> statx.statx('some/file').btime
1577040283.7037938
```
