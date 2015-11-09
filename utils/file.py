# -*- coding: utf-8 -*-
import os
import codecs

def copy(oldPath, newPath, position):
	#python文件打开方式
	# 'r' 		 只读（文件必须存在）
	# 'w' 		 只写(文件不存在则创建)
	# 'a' 		 追加(文件不存在则创建)
	# 'r+'('w+') 读写方式
	# 'a+' 		 追加和读写方式
	oldFile = codecs.open(oldPath,'r','utf-8')
	# newFile = codecs.open(newPath,'w','utf-8')
	
	#文件指针相对偏移
	#os.SEEK_SET(0)  相对文件起始位置
	#os.SEEK_CUR(1)  相对文件当前位置
	#os.SEEK_END(2)  相对文件结束位置
	oldFile.seek(position, os.SEEK_SET)
	# newFile.seek(position, os.SEEK_SET)

	line = oldFile.readlines()

	
	# newFile.write(u'中文')

	if file.closed==False:
		oldFile.close()