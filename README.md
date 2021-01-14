Normal behavior gives at most 2/3 results correct.

```
$ PYTHONPATH=./:third_party/version1 python3 myversion/mymodel.py                        
Got      2, 3, 1
Expected 2, 0, 1
$ PYTHONPATH=./:third_party/version2 python3 myversion/mymodel.py                        
Got      0, 0, 1
Expected 2, 0, 1
$ PYTHONPATH=./ python3 myversion/mymodel.py 
Traceback (most recent call last):
  File "myversion/mymodel.py", line 1, in <module>
    from third_party.version1.model import process as process1
  File "/home/ilyak/Documents/bazel_demo/third_party/version1/model.py", line 1, in <module>
    import util
ModuleNotFoundError: No module named 'util'
```

After setting up bazel, still same problem:
```
$ bazel build mymodel
$ ./bazel-bin/mymodel
Got      2, 3, 1
Expected 2, 0, 1
```