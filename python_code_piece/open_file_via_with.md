# 使用with打开文件

```python
# 打开文件
with open(src, 'rb') as fsrc:
    with open(dst, 'wb') as fdst:
        copyfileobj(fsrc, fdst)
```
