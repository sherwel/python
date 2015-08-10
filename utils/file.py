# -*- coding: utf-8 -*-


def copy(oldPath, newPath):
	#python文件打开方式
	# 'r' 		 只读（文件必须存在）
	# 'w' 		 只写(文件不存在则创建)
	# 'a' 		 追加(文件不存在则创建)
	# 'r+'('w+') 读写方式
	# 'a+' 		 追加和读写方式
	file = open(oldPath,'r',1024)
	for line in file.readlines():
		print line
	file.close()