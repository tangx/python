# 判断操作系统类型


```python

import os
if os.name == "posix":															# Check the os, if it's linux then
    myping = "ping -c 2 "															# This is the ping command
elif os.name in ("nt", "dos", "ce"):											# Check the os, if it's windows then
    myping = "ping -n 2 "	
    
```
