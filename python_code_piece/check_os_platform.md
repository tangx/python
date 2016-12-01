# 判断操作系统类型

## 使用 `os.name` 判断

```python

import os
if os.name == "posix":															# Check the os, if it's linux then
    myping = "ping -c 2 "															# This is the ping command
elif os.name in ("nt", "dos", "ce"):											# Check the os, if it's windows then
    myping = "ping -n 2 "	
    
```


## 使用 `sys.platform` 判断

该片段是用来在不同系统环境下导入加密模块的

> https://github.com/geekcomputers/Python/blob/master/password_cracker.py

```
from sys import platform as _platform

# Check the current operating system to import the correct version of crypt
if _platform == "linux" or _platform == "linux2":
    import crypt # Import the module
    # print "Unix-like"
elif _platform == "darwin":
    # Mac OS X
    import crypt
    # print "Mac OS X"
elif _platform == "win32":
    # Windows
    # print "Windows"
    try:
       import fcrypt # Try importing the fcrypt module
    except ImportError:
       print 'Please install fcrypt if you are on Windows'
```