# -*- coding: utf-8 -*-
import json

data = ["a","b",{"c":u"测试"}]
print repr(data)


#python对象转化为json
result = json.dumps(data, ensure_ascii=False)
print type(result)
print result

#json字符串反解析成python对象
data = json.loads(result)
print type(data)
print data


