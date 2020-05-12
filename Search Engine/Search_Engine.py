#!/usr/bin/env python
# coding: utf-8

# In[1]:


from konlpy.tag import Kkma
import math
#log10(int)

#print(kkma.pos("아버지가방에들어가신다"))
#['아버지', '가방', '에', '들어가', '시', 'ㄴ다']

kkma = Kkma()


# In[2]:


#f = open('.\list.txt','r', encoding='UTF-8') 
import os 
path = '.\\1000_news\\'
f_list = os.listdir(path)
print(len(f_list))
print(f_list[:10])
print(path + f_list[0])


# In[3]:


# file read

terms = []          #set of terms   #word vector 
term_file_cnt = []  # cnt of file which has terms(index)  #단어가 나온 파일의 수
term_freq = []      #freq of terms in each files
file_cnt = 0

for txt in f_list:
    try:
        file = open(path + txt, 'r', encoding='cp949')
    except UnicodeDecodeError:
        print(path + txt)
    file_cnt += 1
    s = set()
    file_terms_cnt = 0      #cnt of terms in a file #파일에 있는 단어의 수 
    term_cnt = {}          #freq of terms in a file #
    tmp = {}
    while(True):
        try:
            line = file.readline()
        except UnicodeDecodeError:
            print(path + txt[:-1])
            continue

        if not line:
            file.close()
            break
        
        if( len(line[:-1])<=10):
            continue
        try:
            morphs = kkma.morphs(line[:-1])
        except :
            print(line[:-1] + "line end")
        
        for m in morphs:
            file_terms_cnt += 1
            if( m not in s):
                s.add(m)
            if( m not in terms):
                terms.append(m)
                term_file_cnt.append(0)
                
            term_cnt[terms.index(m)] = term_cnt.get(terms.index(m),0) + 1

        
    for k,v in term_cnt.items():
        tmp[k] = v/file_terms_cnt
    term_freq.append(tmp)

    l = list(s)
    for m in l:
        term_file_cnt[terms.index(m)] += 1
    


# In[4]:


# word ID
f = open('word_ID.txt','w') 
for t in terms:
    f.write(t + '\n')
f.close()


# In[5]:


#print(term_file_cnt)


# In[6]:


print(term_freq[0]) #문서에 대한 단어 index:가중치 


# In[7]:


#forward index, backward indexing
backward_index = [{} for i in range(len(terms))]


# In[8]:


# tf * idf
f = open('tf-idf.txt','w') 
for i in range(len(term_freq)):
    for w_id,v in term_freq[i].items():
        tf_idf = v*math.log10(file_cnt/term_file_cnt[k])
        f.write('{}:{} '.format(w_id, tf_idf) )
        backward_index[w_id][i]=(tf_idf)
    f.write('\n')
f.close()


# In[9]:


print(backward_index[0])  # 단어에 대한 문서-가중치 
# 0번 단어는 0~10번, 17번 21번 문서에 존재 


# In[10]:


term_table = []
posting_file = []
loc_of_files = 0

#backward_index
f = open('backward_index.txt','w')
for word in backward_index:
    n_of_files = 0
    for file,v in word.items():
        f.write('{}:{} '.format(file, v))

        term_table
        posting_file.append([file, v])
        n_of_files += 1

    term_table.append([loc_of_files, n_of_files])
    loc_of_files += n_of_files
    
    f.write('\n')
f.close()


# In[11]:


f = open('posting_file.txt','w')
for doc,weight in posting_file:
    f.write('{} {}'.format(doc, weight))
    f.write('\n')
f.close()


# In[12]:


print(term_table[:10]) 
# 0번 단어는 0부터 322개  # 1번 단어는 322 부터  245개 
#상위 10개만 출력


# In[13]:


print(posting_file[320:330]) 
# 0번 단어에 대한 문서-가중치 : 133 까지  / 1번 단어에 대한 문서-가중치 : 134 부터 
#경계 값을 보기위해 134 근처 출력 


# In[ ]:





# In[22]:


#keyword 검색

keyword = list(map(str, input()[:].split(' ') ) )
#keyword = kkma.morphs(str(input()))
print(keyword)


# In[15]:


#keyword 헤 해당하는 word id 
keyword_index = [terms.index(k) for k in keyword if k[0] != '-']
print(keyword_index) 

removal_keyword_index = [terms.index(k[1:]) for k in keyword if k[0]=='-'] # 검색 제외할 문서  


# In[16]:


#termtable 검색한 결과 
result_term_table = [term_table[i] for i in keyword_index]
print(result_term_table)

result_term_table_removal = [term_table[i] for i in removal_keyword_index] # 제외할 문서->tremtable 검색


# In[17]:


#posting_file 검색 결과 
result_posting_file_removal = [posting_file[idx:idx+cnt] for idx, cnt in result_term_table_removal ] # 제외 할 문서->posting file  
result_removal_file = [idx for word in result_posting_file_removal for idx,weight in word] # 제외 할 doc id 목록

result_posting_file = [ posting_file[idx:idx+cnt] for idx, cnt in result_term_table ]
print(result_posting_file)
#calc_weight = [  for idx, cnt in result_term_table for file_idx, w in posting_file[idx:idx+cnt] ]
#term_cnt[terms.index(m)] = term_cnt.get(terms.index(m),0) + 1


# In[18]:


calc_weight = {}
for idx, cnt in result_term_table:
    for file_idx, w in posting_file[idx:idx+cnt]:
        if(file_idx in result_removal_file):# * 
            continue # * 
        calc_weight[file_idx] = calc_weight.get(file_idx, 0) + w
print( calc_weight )


# In[19]:


result_calc_weight = [[w, file_idx] for file_idx, w in calc_weight.items() if w >= 0.01 ]
result_calc_weight.sort(reverse = True)
print(result_calc_weight[:])


# In[20]:


search_result = [ f_list[i[1]] for i in result_calc_weight]
print(search_result[:])


# In[ ]:





# In[21]:


while(True) :
    i=input('i : 읽을 문서 번호, enter : stop')
    if( i== '' or i == 'enter'):
        break
    try : 
        i = int(i) - 1
    except: 
        print('enter number or enter')
        continue
    f = open(path+search_result[i], 'r')
    while(True):
        line = f.readline()
        if not line:
            f.close()
            break
        if( len(line)<10):
            continue
        print(line)
        


# In[ ]:




