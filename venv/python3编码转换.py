#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

text = "我是文本"

turn_text = text.encode()
print(turn_text)
print(type(turn_text))
# --> b'\xe6\x88\x91\xe6\x98\xaf\xe6\x96\x87\xe6\x9c\xac'
# --> <class 'bytes'>

return_text = turn_text.decode()
print(return_text)
print(type(return_text))
# --> 我是文本
# --> <class 'str'>

bytes.decode(encoding="utf-8", errors="strict")
str.encode(encoding="utf-8", errors="strict")

˜