#tf-idf 계산, 유사도 계산
import math
from ast import literal_eval

f = open('morph_analysis_result.txt')

origin_sentence = f.readline()
input_sentence = literal_eval(f.readline())
n_print = int(f.readline())

total_morph = int(f.readline())
sentence_cnt_of_morph_appear = []
for i in range(total_morph):
	sentence_cnt_of_morph_appear.append(int(f.readline()))

total_lines = int(f.readline())

input_tfidf = dict()
for key, val in input_sentence.items():
	tf = val / sum(list(input_sentence.values()))
	idf = math.log10(total_lines / sentence_cnt_of_morph_appear[key]) 
	
	input_tfidf[key] = tf*idf

similarity = []

for i in range(total_lines):
	line = f.readline() 
	sentence = literal_eval(line)
	
	#tfidf 
	tfidf = dict()
	for key, val in sentence.items():
		tf = val / sum(list(sentence.values())) #문장에서 단어 빈도
		idf = math.log10( total_lines / sentence_cnt_of_morph_appear[key] ) #전체중에 얼마나 나왔는지
		tfidf[key] = tf*idf
		
	#유사도
	cosine_sim = 0
	for key, val in tfidf.items():
		cosine_sim += min(val, input_tfidf.get(key,0)) 
		
	cosine_sim /= math.sqrt( sum([val*val for key, val in tfidf.items()]) * sum([val*val for key,val in input_tfidf.items()]) )
	
	similarity.append((i, cosine_sim))
	
similarity.sort(reverse = True, key = lambda s:s[1])

f.close()

f = open('KCC150_K01_utf8.txt')
sentence_list = []
for i in range(total_lines):
	sentence_list.append(f.readline())
f.close()

for i in range(n_print):
	print("{}\t{}".format(i+1, sentence_list[similarity[i][0]] ) )
	
		
		
		

