from khaiii import KhaiiiApi
api = KhaiiiApi()


for i in range(10):
	s = str(input())
	
	res = []
	for word in api.analyze(s):
		res.append(str(word))
	res = [word.split('\t')[1] for word in res]
	
	print(res)
	
	
