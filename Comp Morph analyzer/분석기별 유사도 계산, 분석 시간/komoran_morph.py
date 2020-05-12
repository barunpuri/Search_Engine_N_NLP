from konlpy.tag import Komoran
komo = Komoran()

import time

print( '한글 문장 입력: ')
input_origin = str(input())

# 출력할 문장 수 
n = 10 

#timer start
start = time.time()

f = open('KCC150_K01_utf8.txt') # 

word = []	#형태소 list
sentence_morph_list = []	#각 문장을 형태소 분석한 결과, 출현 횟수
sentence_cnt_of_morph_appear = [] 	#각 형태소가 출현한 문서 수 

# % 출력
total_lines = 1000000
line_cnt = 0
percent = 0

#입력 문장
input_morph = dict()
for m in komo.morphs(input_origin):
    if(m not in word):
        word.append(m)
        sentence_cnt_of_morph_appear.append(0)
    morph_index = word.index(m)
    input_morph[morph_index] = input_morph.get(morph_index,0) + 1
    
    for key,val in input_morph.items():
    	sentence_cnt_of_morph_appear[key] += 1

#word embedding, 형태소 분석
while(True):
    line_cnt += 1
    if( int(100 * line_cnt / total_lines) != percent):
	percent += 1
	print("current\t{}% take\t{}s".format(percent, time.time()-start ))
		
    line = f.readline()
    if not line:
	f.close()
	break
		
    sentence_morph = dict()
    morph = komo.morphs(line)
    for m in morph: 
	if( m not in word ):
	    word.append(m)
	    sentence_cnt_of_morph_appear.append(0)
			
	morph_index = word.index(m)
	sentence_morph[morph_index] = sentence_morph.get(morph_index,0) + 1
	
    for key,val in sentence_morph.items():
	sentence_cnt_of_morph_appear[key] += 1
    
    sentence_morph_list.append(sentence_morph)
		
time_taken = time.time() - start
print('morphological analysis time: {}s'.format(time_taken))

f.close()

f = open('morph.txt', 'w')
for m in word:
    f.write(m +'\n')
f.close()

f = open('morph_analysis_result.txt', 'w')
f.write(str(input_origin) +'\n')
f.write(str(input_morph) +'\n')
f.write(str(n) +'\n')
f.write(str(len(word)) +'\n')
for n in sentence_cnt_of_morph_appear:
    f.write(str(n) +'\n')
f.write(str(total_lines) +'\n')
for sentence in sentence_morph_list:
    f.write(str(sentence) +'\n')
f.close()




