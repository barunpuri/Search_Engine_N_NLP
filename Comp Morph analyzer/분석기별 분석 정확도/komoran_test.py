from konlpy.tag import Komoran
komo = Komoran()

for i in range(10):
	s = str(input())
	
	print( komo.pos(s) )
	
	
