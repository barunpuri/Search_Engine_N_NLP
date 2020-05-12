# Search Engine

### 문서집합 : 신문기사 383개 및 IT 분야 뉴스 1,000개 파일
### 구현방법 : 
1) 각 문서에 대해 Doc. ID 부여 -- DocID table 생성
2) forward indexing, backward indexing
3) term table과 posting file로 분리하여 저장
4) 

### Files
- Search_Engine.py : 실행파일

# Comp Morph analyzer
형태소 분석기 비교 


## 1. 분석 성능 비교 
### 비교방법 : 특정 문자을 넣어 분석기별 성능 비교 
### Files
- 분석기별 분석 정확도
    - khaiii_test.py : khaiii 분석기 사용
    - khaiii_test.py : khaiii 분석기 결과 
    - komoran_test.py : komoran 분석기 사용
    - komoran_test.py : komoran 분석기 결과 
    - mecab_test.py : mecab 분석기 사용
    - mecab_test.py : mecab 분석기 결과 

## 2. 분석 시간 비교 
### 분석문서 : 약 100만 문장
### 비교방법 :
1) 대용량 문장 워드 임베딩
2) 벡터 유사도 계산
3) 유사한 문장 추출
### Files
- 분석기별 유사도 계산, 분석 시간


## 발표 영상
[![Watch the video](https://img.youtube.com/vi/YJ4nLarCo2E/maxresdefault.jpg)](https://youtu.be/YJ4nLarCo2E)
<https://youtu.be/YJ4nLarCo2E> 