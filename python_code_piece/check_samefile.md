# 判断两个文件是否为相同文件

在 unix-like 操作系统中， python 判断两个文件是否使用同一个 `inode` 。
在 windows 操作系统中， python 判断两个文件的路径是否一致。


## 创建文件

```bash
ln get-pip.py get-pip.py.2
cp -a get-pip.py get-pip.py.3
ln -s get-pip.py get-pip.py.link
```

## 测试文件是否相同

```python

import os
f1 = '/root/get-pip.py'
f2 = '/root/get-pip.py.2'
f3 = '/root/get-pip.py.3'
flink = '/root/get-pip.link'


def is_samefile(f1,f2):
    if os.path.samefile(f1, f2):
        print "yes, the samefile"
    else:
        print "no, not the samefile"


is_samefile(f1,f2)
# yes, the samefile

is_samefile(f1,f3)
# no, not the samefile

is_samefile(f1,flink)
# no, not the samefile

```


## 创建判断相同文件函数

```python
# 判断文件是否相同
# hasattr
# os.path.samefile
def _samefile(src, dst):

    # Macintosh, Unix.
    if hasattr(os.path, 'samefile'):
        try:
            return os.path.samefile(src, dst)
        except OSError:
            return False

    # All other platforms: check for same pathname.
    return (os.path.normcase(os.path.abspath(src)) ==
            os.path.normcase(os.path.abspath(dst)))

```
