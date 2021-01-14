Normal behavior only gives 2/3 results correct.

$ PYTHONPATH=./:third_party/version1 python3 myversion/mymodel.py                        
(2, 3, 1)
Expected 2, 0, 1
$ PYTHONPATH=./:third_party/version2 python3 myversion/mymodel.py                        
(0, 0, 1)
Expected 2, 0, 1
