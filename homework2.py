import os
import hashlib

lst = {}
def walk(dirname):
	
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		if os.path.isfile(path):
			if os.path.splitext(path)[1] == '.txt':
				text = open(path,'rb')
				hl = hashlib.md5()
				hl.update(text.read())
				hash_code = hl.hexdigest()
				text.close()
				md5 = str(hash_code).lower()
				if len(md5) != 0:
					lst[path]=md5
				
		else:
			walk(path)
	
walk('/Users/lyuhuanyi/Desktop')

val ={}

for key,value in lst.items():
	if value not in val:
		val[value] = [key]
	else:
		val[value].append(key)

for k,v in val.items():
	if len(v) > 1:
		print(v)
