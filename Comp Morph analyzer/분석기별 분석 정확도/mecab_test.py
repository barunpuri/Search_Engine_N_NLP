import MeCab
m = MeCab.Tagger('-d ./mecab-ko-dic-2.1.1-20180720/')

for i in range(10):
	s = str(input())
	res = m.parse(s)
	
	res = res[:-5].split('\n')
	res = [word.replace('\t', '/') for word in res]
	res = [word.split(',')[0] for word in res]
	
	print(res)

